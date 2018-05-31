from subprocess import Popen, call, PIPE
import os
import sys
import json
import glob
import argparse
import webbrowser
import fileinput
import time
from random import randint
import socket
from threading import Thread
from collections import defaultdict





mappings = defaultdict(list)
mappings = {}
ports = []
types = defaultdict(list)
types = {'images': [], 'videos': [], 'audios': [], 'texts': [], 'others': []}


class Th(Thread):
    def __init__(self, entrypoint, port):
        Thread.__init__(self)
        self.entrypoint = entrypoint
        self.port = port

    def run(self):
        time.sleep(3)
        webbrowser.open_new_tab("http://" + self.entrypoint + ":" + str(self.port))


def get_args():
    read_file = open('settings.json', 'r')
    data = json.load(read_file)
    return data['entrypoint'], data['port']


def save_args(entry, port):
    data = {
        'entrypoint': entry,
        'port': str(port),
    }
    with open('settings.json', 'w') as outfile:
        json.dump(data, outfile)


def command_line_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('--entrypoint', '-e',
                        dest='entrypoint',
                        default='127.0.0.1',
                        type=str,
                        help='Entrypoint of main server. Default = 127.0.0.1')
    parser.add_argument('--port', '-p',
                        dest='port',
                        default=8001,
                        type=int,
                        help='Port of main server. Default = 80')

    return parser.parse_args()


def start(entrypoint, port):
    activate_this = '../SmartDiF/bin/activate_this.py'
    exec (open(activate_this).read(), dict(__file__=activate_this))
    browser = Th(entrypoint, port)
    browser.start()
    call('gunicorn --workers=1 --threads=5 --worker-class eventlet --max-requests=5 --timeout=30 --bind ' + entrypoint + ":" + str(
        port) + ' myproject.wsgi:application', shell=True)


def fill_mappings():
    file_list = [f for f in glob.iglob('techniques/*/settings.json') if os.path.isfile(f)]
    for f in file_list:
        with open(f) as data_file:
            data = json.load(data_file)
            mappings[data['name']] = {'image': data['image_name'], 'virtualization': data['virtualization']}
    return mappings


def fill_types():
    file_list = [f for f in glob.iglob('techniques/*/settings.json') if os.path.isfile(f)]
    for f in file_list:
        with open(f) as data_file:
            data = json.load(data_file)
            if data['type'] == 'image':
                types['images'].append(data['name'])
            elif data['type'] == 'video':
                types['videos'].append(data['name'])
            elif data['type'] == 'audio':
                types['audios'].append(data['name'])
            elif data['type'] == 'text':
                types['texts'].append(data['name'])
            else:
                types['others'].append(data['name'])
    return types


def load_containers():
    try:
        if os.stat("containers.json").st_size > 2:
            data = json.load(open('containers.json'))
            return data
        else:
            return {}
    except FileNotFoundError:
        return {}


def save_containers(data):
    with open('containers.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    args = command_line_parsing()
    save_args(args.entrypoint, args.port)
    start(args.entrypoint, args.port)
