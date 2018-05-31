from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
import hashlib
import datetime
import requests
import json
import os
import sys
import time
from subprocess import Popen, PIPE
import urllib
import copy
from SmartDiF import fill_types, fill_mappings,save_containers,load_containers, get_args
from collections import defaultdict
from django.contrib import messages
import string
import random
import socket
from random import randint
from subprocess import check_output

args = get_args()
mappings = fill_mappings()
types = fill_types()
containers = load_containers()
entrypoint = args[0]
port = args[1]
technique = 'null'
lastcontainer = 'null'



def check(name):
    # parts[1] is the image name, parts[11] is container name
    out = check_output(["docker", "ps", "-a", "-f", "ancestor="+name]).decode(sys.stdout.encoding).splitlines()
    global containers
    i = 0
    j = 1
    count = 0
    image = 0
    container = 0
    check_msg = "Existe uma imagem que não foi criada pela ferramenta"
    # check freq of images
    for line in out:
        parts = line.split()
        if len(parts) >= 1 and i > 0:
            count += 1
        i += 1
    print(count)
    if count == 1:
        for line in out:
            parts = line.split()
            if len(parts) >= 1 and j == i:
                if "smartdifdocker/tecnicas:"+name in parts:
                    # image exist and container too
                    container = 1
                    image = 1
                    print("Linha 68")
                else:
                    # container exist, but not created by tool
                    container = 0
                    print("Linha 72")
            j += 1
    elif count > 1:
        check_msg = "Existe pelo menos uma imagem que não foi criada pela ferramenta, favor verificar"
    else:
        check_msg = "Not created"
    if container == 1 and image == 1:
        check_msg = "Created"
        return check_msg
    elif image == 1 and container == 0:
        check_msg = "Existe pelo menos uma imagem em um container que não foi criado pela ferramenta, favor verificar"
        return check_msg
    else:
        return check_msg
    return check_msg


def check_status(port):
    try:
        status = urllib.request.urlopen('http://localhost:'+str(port))
        if status.getcode() == 200:
            return 1
    except urllib.error.HTTPError as e:
        if e.code == 111:
            check_status(port)
    except urllib.error.URLError as e:
        if e.reason != '':
            check_status(port)


def tecnicas_ativas(request):
    if request.method == 'POST':
        global containers
        if containers is not None:
            resultado = copy.deepcopy(containers)
            for  name in resultado:
                resultado[name]['id'] = hashlib.sha256(resultado[name]['id'].encode()).hexdigest()
            return JsonResponse(resultado)
        else: 
            return JsonResponse("null")





def fill_url(port_container,name):
    global mappings
    write_file = open('techniques_urls.py', 'w')
    write_file.write('from django.conf.urls import url \nfrom httpproxy.views import HttpProxy\n\nurlpatterns = [ \n')
    write_file.write("url(r'^" + name + "/(?P<url>.*)$',HttpProxy.as_view(base_url='http://127.0.0.1:" + str(port_container) + "/'))," + "\n")
    write_file.write("]")
    write_file.close()


def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1', port))
    if result == 0:
        return check_port(randint(26490, 26999))
    else:
        return port
    s.close()


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def finishAll(request):
    if request.method == 'POST':
        global containers
        for name in containers:
            Popen("docker rm -f " + containers[name]['id'], shell=True)
        containers = {}
        save_containers(containers)
        return JsonResponse({'resposta': "sucess"})


def finish(request):
    if request.method == 'POST':
        global containers
        json_data = json.loads(request.body.decode("utf-8"))
        name = json_data['tecnica_nome']
        id_hash = json_data['id']
        print("No finish "+check(name))
        print("\nNo finish "+name)
        print("\nNo finish "+id_hash)

        if check(name) == "Created":
            print("\nNo finish imagem criada")
            print("\n No finish, valor do hash do container:"+hashlib.sha256(containers[name]['id'].encode()).hexdigest())
            print("\n No finish, valor do hash do POST:"+id_hash)

            if id_hash == hashlib.sha256(containers[name]['id'].encode()).hexdigest():
                print ("\n No finish id has correto")
                Popen("docker rm -f " + containers[name]['id'], shell=True)
                del containers[name]
                save_containers(containers)

                return JsonResponse({'resposta': "sucess"})
            else:
                return JsonResponse({'resposta': "fail-1"})
        else:
            return JsonResponse({'resposta': "fail-2"})


def dispatcher(request):
    global mappings
    global containers
    global args
    global technique
    global lastcontainer
    if request.method == 'POST':
        json_data = json.loads(request.body.decode("utf-8"))
        name = json_data['tecnica_nome']
        print (name)

        for map in mappings:
            if map == name:
                print("Linha 117")
                port_container = check_port(26490)
                image = mappings[map]['image']
                virtualization = mappings[map]['virtualization']
                fill_url(port_container,map)
                print(str(port))
                if check(image) == "Not created":
                    id = id_generator(10, str(randint(len(image), len(image) * 2)) + image.upper() +
                                      str(randint(len(image) * 2, len(image) * 4)))
                    if virtualization == 'docker':
                        Popen("docker run --rm --network host -e ID="+id+" -e PORT="+str(port_container)+" --name " + id + " --expose " + str(port_container) + " smartdifdocker/tecnicas:" + image, shell = True)

                    elif virtualization == 'vm':
                        print("Criando VM")
                    containers[image] = {'id':id,'port':port_container}
                    save_containers(containers)
                    time.sleep(5)
                    id_hash = hashlib.sha256(id.encode()).hexdigest()
                    return JsonResponse({'id': id_hash,'porta':str(port_container),'resposta':"sucess"})
                elif check(image) == "Created":
                    id = containers[image]['id']
                    id_hash = hashlib.sha256(id.encode()).hexdigest()
                    print("Linha 199")
                    return JsonResponse({'id': id_hash,'porta':str(port_container),'resposta':"sucess"})
                else:
                    return JsonResponse({'id':"none",'resposta':check(image)})



def home(request):
    global types
    return render(request, 'analisador/index.html',
                  {'tituloimagem': types['images'], 'titulovideo': types['videos'], 'tituloaudio': types['audios'],
                   'titulotexto': types['texts'], 'titulooutros': types['others'], }, )


def sobre(request):
    return render(request, 'analisador/sobre.html')

def loading(request):
    return render(request, 'analisador/loading.html')












