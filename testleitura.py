from subprocess import Popen, call, PIPE
from subprocess import check_output
import os
from collections import defaultdict
import string
import random
import sys
import time
import urllib.request
from random import randint
from SmartDiF import load_containers
containers = load_containers()


def check(name):
        # parts[1] is the image name, parts[11] is container name
        out = check_output(["docker", "ps", "-a", "-f", "ancestor=" + name]).decode(sys.stdout.encoding).splitlines()
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
                    print(parts[11])
                    if parts[11] in containers[name]:
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


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def check_status(port):
    print('test')
    try:
        status = urllib.request.urlopen('http://google.com.br')
        print(status.getcode())
        if status.getcode() != 200:
            check_status(port)
    except urllib.error.HTTPError as e:
        print('111')
        check_port(port)
    except urllib.error.URLError as e:
        print(e.reason)
        if e.reason != '':
            print('linha 78')
    return time.sleep(1)

def check_container():
    out = check_output(["docker", "ps", "-a"]).decode(sys.stdout.encoding).splitlines()
    container_name = []
    i = 0
    for line in out:
        parts = line.split()
        if len(parts) >= 1 and i > 0:
            container_name.append(parts[11])
        i += 1
    for container in container_name:
        print(container)

if __name__ == "__main__":
    container = {'imagem1':{'id':'BANANA'}}
    container['imagem2'] = {'id':'MAÇÃ'}
    for name in container.values():
        print(name['id'])


