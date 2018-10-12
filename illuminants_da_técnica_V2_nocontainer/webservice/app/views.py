from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import ImagemForm, FacesForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import imagem, audio, outros, texto, video, UploadImage
from django.core.urlresolvers import reverse
from subprocess import Popen, call, PIPE
import json
import sys
import time
import glob
from shutil import copy
import requests
from PIL import Image
import os
from django.conf import settings
from subprocess import check_output
from collections import defaultdict
from importlib import util
from tifs2016.source_code.classifySVMCetico import fullClassification




nome_file = ""


@csrf_exempt
def home(request):
    if request.method == 'POST':
        global nome_file
        form = ImagemForm(request.POST, request.FILES)
        print("POST")
        if form.is_valid():

            print("FORM IS VALID")
            iic_key = True;
            gge_key = True;
            img = UploadImage(imagem=request.FILES['resultado'])
            database = Image.open(img.imagem)
            command = "rm "+ settings.BASE_DIR + "/tifs2016/data-base/images/*"
            call(command, shell=True)
            database.save(settings.BASE_DIR + '/tifs2016/data-base/images/' + img.imagem.url.replace("/media/","").replace("%20","_").replace("(","_").replace(")","_"))
            nome_file = img.imagem.url.replace("/media/","").replace("%20","_").replace("(","_").replace(")","_").split(".")
            nome_file = nome_file[0]
            print (nome_file)
            segment = Popen("python3 tifs2016/source_code/segmentAllImagesForIlluminantMethod.py", shell=True)
            segment.wait();
            iic = Popen("python3 tifs2016/source_code/extractIICMaps.py", shell=True)
            iic.wait();
            while (iic_key):
                for pngfile in glob.iglob(os.path.join(settings.BASE_DIR + "/tifs2016/data-base/IIC/", "*.png")):
                    if os.path.isfile(pngfile):
                        copy(pngfile, settings.BASE_DIR + "/static/IIC/")
                        iic_key = False;

            gge = Popen("python3 tifs2016/source_code/extractGGEMaps.py", shell=True)
            gge.wait();
            while(gge_key):
                for pngfile in glob.iglob(os.path.join(settings.BASE_DIR + "/tifs2016/data-base/GGE/", "*.png")):
                    if os.path.isfile(pngfile):
                        copy(pngfile, settings.BASE_DIR + "/static/GGE/")
                        gge_key = False;

            return render(request, 'app/Illuminantes.html', {'form': form})
        else:
            print("HELLO")
            print(form.errors)
    else:
        form = ImagemForm()

    return render(request, 'app/Illuminantes.html', {'form': form} )


def resultado(request):
    if request.method == 'POST':
        i = 1
        global nome_file
        command = "rm "+settings.BASE_DIR +"/tifs2016/face-positions/*"
        call(command, shell=True)
        json_data = json.loads(request.body.decode("utf-8"))
        descritores = json_data['descritores']
        if (descritores == ''):
            descritores = "ACC BIC LCH CCV EOAC SPYTEC SASI LAS UNSER"
        print(json_data)
        for data in json_data['faces_positions']:
            normal_file = open(settings.BASE_DIR + '/tifs2016/face-positions/'+nome_file+'.txt', 'a')
            normal_file.write(str(i) + "	NORMAL	"+str(format(data['minX'], '.0f'))+"	"+str(format(data['maxX'],'.0f'))+"	"+str(format(data['minY'],'.0f'))+"	"+str(format(data['maxY'],'.0f'))+"\n")
            i += 1
        normal_file.close()
        if os.path.isfile(settings.BASE_DIR + '/tifs2016/face-positions/'+nome_file+'.txt'):
            print (descritores.upper())
            extract = Popen("python3 tifs2016/source_code/extractAllFeatureVectors.py \"%s\"" % descritores,shell=True)
            extract.wait();

            resultado = fullClassification(nome_file,descritores.split(" "))


        return JsonResponse({'resultado': resultado})
