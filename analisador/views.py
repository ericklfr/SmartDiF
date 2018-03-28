from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageDraw, ImageFilter, ImageTransform, ImageOps
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from .forms import ImagemForm, GrauForm, ImagemTForm, ImagemCForm
from .models import UploadImage, imagem, audio, outros, texto, video
from django.core.mail import send_mail
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
import datetime
import requests
import json
import os
import sys
import time
from subprocess import Popen, PIPE
import urllib
from rest_framework.views import APIView
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

print('Containers:'+str(containers))


@csrf_exempt
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
                if name in parts:
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


def fill_url(port_container,name):
    global mappings
    write_file = open('techniques_urls.py', 'w')
    write_file.write('from django.conf.urls import url \nfrom httpproxy.views import HttpProxy\n\nurlpatterns = [ \n')
    write_file.write(
        "url(r'^" + mappings[name]['url'] + "(?P<url>.*)$',HttpProxy.as_view(base_url='http://" + mappings[name][
                'endpoint'] + ":" + str(port_container) + "/'))," + "\n")
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


def finish(request,name,id):
    global containers
    print('INICIO')
    print(name)
    print(id)
    print(check(name))
    if check(name) == "Created":
        print("hello guys")
        Popen("docker rm -f " + id, shell=True)
        # key is the name of tecnique
        for key in containers.values():
            if id == key['id']:
                print("linha 146")
                del containers[name]
                save_containers(containers)
                break
    return HttpResponseRedirect('/')


class MyMiddleware:
    global technique
    global entrypoint
    global containers
    global port

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['entrypoint'] = entrypoint
        response['port'] = port
        return response


def dispatcher(request, name):
    global mappings
    global containers
    global args
    global technique
    global lastcontainer
    for map in mappings:
        if map == name:
            print("Linha 117")
            url = mappings[map]['url']
            port_container = check_port(26490)
            image = mappings[map]['image']
            virtualization = mappings[map]['virtualization']
            fill_url(port_container,map)
            print(str(port))
            if check(image) == "Not created":
                id = id_generator(10, str(randint(len(image), len(image) * 2)) + image.upper() +
                                  str(randint(len(image) * 2, len(image) * 4)))
                if virtualization == 'docker':
                    Popen("docker run --rm --network host -e NAME="+image+" -e ID="+id+" -e PORT="+str(port_container)+" --name " + id + " --expose " + str(port_container) + " " + image, shell = True)

                elif virtualization == 'vm':
                    print("Criando VM")
                containers[image] = {'id':id}
                save_containers(containers)
                '''check_status(port_container)'''
                time.sleep(5)
                return HttpResponseRedirect('/' + url)
            elif check(image) == "Created":
                print(url)
                print("Linha 199")
                return HttpResponseRedirect('/' + url)
            else:
                messages.info(request, check(image))
                return render(request,'analisador/index.html',{"messages":check(image)})

    return HttpResponseRedirect('/')


def home(request):
    global types
    return render(request, 'analisador/index.html',
                  {'tituloimagem': types['images'], 'titulovideo': types['videos'], 'tituloaudio': types['audios'],
                   'titulotexto': types['texts'], 'titulooutros': types['others'], }, )


def somar_test(request):
    if request.method == 'POST':
        form = Somar(request.POST, 'analisador/somar_resultado')
        if form.is_valid():
            return render(request.GET, 'analisador/somar_resultado.html', context)

    else:
        form = Somar()
    return render(request, 'analisador/somar.html', {'form': form})



'''
def somar(request):

    if request.method == "POST":
        form = Somar(request.POST)
        if form.is_valid():
            data = {'valor1':form.cleaned_data['valor1'],'valor2':form.cleaned_data['valor2']}
            headers = {'Content-type': 'application/json'}
            os.system("docker run --rm --network host --name container01 --expose 8004 tecnica01")
            r = requests.post('http://localhost:8004/api/test/',json=data,headers=headers)
            if r:
                os.system("docker kill --signal="+"SIGINT"+" container01")
                resultado = r.json()
                return render(request,'analisador/resultado.html',{'resultado':resultado['resultado']})
    else:
        form = Somar()

    return render(request, 'analisador/somar.html', {'form': form})'''


def pretoebranco(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.convert('L')
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg, 'form': form},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/pretoebranco.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def rotacionarmanual(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        form2 = GrauForm(request.POST)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            novograu = RotImage(grau=request.POST['resultado'])
            converter = Image.open(novaimg.imagem)
            converter = converter.rotate(int(novograu.grau))
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
        form2 = GrauForm
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/rotacionarmanual.html', {'imagens': imagens, 'form': form, 'form2': form2},
                              context_instance=RequestContext(request))


def Iluminantes(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            context = {'novaimg': novaimg}
            return render(request, 'analisador/resultado.html', context)

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render(request, 'analisador/Iluminantes.html', {'imagens': imagens, 'form': form})


def Twitter(request):
    return render_to_response('analisador/Twitter.html',
                              context_instance=RequestContext(request))


def Novo_modelo(request):
    return render_to_response('analisador/novo_modelo.html',
                              context_instance=RequestContext(request))


def Detalhes(request):
    return render_to_response('analisador/detalhes.html',
                              context_instance=RequestContext(request))


def Modelos(request):
    return render_to_response('analisador/Modelos.html',
                              context_instance=RequestContext(request))


def rotacionar180(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.rotate(180)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/rotacionar180.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def rotacionar270(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.rotate(270)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/rotacionar270.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def horizontal(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = ImageOps.mirror(converter)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/horizontal.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def vertical(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = ImageOps.flip(converter)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    # Render list page with the documents and the form
    return render_to_response('analisador/vertical.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def blur(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.filter(ImageFilter.BLUR)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    # Render list page with the documents and the form
    return render_to_response('analisador/blur.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def smooth(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.filter(ImageFilter.SMOOTH)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    # Render list page with the documents and the form
    return render_to_response('analisador/smooth.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def contour(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.filter(ImageFilter.CONTOUR)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/contour.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def sharpen(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter = Image.open(novaimg.imagem)
            converter = converter.filter(ImageFilter.SHARPEN)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/sharpen.html', {'imagens': imagens, 'form': form},
                              context_instance=RequestContext(request))


def transpor(request):
    if request.method == 'POST':
        form = ImagemTForm(request.POST, request.FILES)
        form2 = ImagemTForm(request.POST, request.FILES)
        if form.is_valid():
            size = (500, 500)
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg2 = UploadImage(imagem2=request.FILES['resultado2'])
            novaimg2.save()
            novaimg.save()
            img1 = Image.open(novaimg.imagem)
            img2 = Image.open(novaimg2.imagem2)

            (w, h) = img1.size
            img1 = img1.resize((w, h), Image.BILINEAR).crop((0, 0, w, h))

            img2 = img2.resize((w, h), Image.BILINEAR).crop((0, 0, w, h))
            img1.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            img2.save(settings.BASE_DIR + '/analisador/' + novaimg2.imagem2.url)
            alpha = 0.5
            converter = Image.blend(img1, img2, alpha)
            converter.save(settings.BASE_DIR + '/analisador/' + novaimg.imagem.url)
            return render_to_response('analisador/resultado.html', {'novaimg': novaimg},
                                      context_instance=RequestContext(request))

    else:
        form = ImagemTForm()
        form2 = ImagemTForm()
    imagens = UploadImage.objects.all()

    return render_to_response('analisador/transpor.html', {'imagens': imagens, 'form': form, 'form2': form2},
                              context_instance=RequestContext(request))


'''

def resultado(request):
    return render(request, 'analisador/resultado.html')'''
