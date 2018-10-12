from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Somar, ImagemForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import imagem, audio, outros, texto, video, UploadImage
from django.core.urlresolvers import reverse
from subprocess import Popen, call, PIPE
import json
import sys
import time
import requests
import os
from subprocess import check_output


@csrf_exempt
def home(request):
    out = os.environ
    id = out.get("ID")
    name = out.get("NAME")
    return render(request, 'app/index.html', {'container_id':id,'technique_name':name})


def ilu(request):
    print(request.META.get('HTTP_REFERER'))
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            novaimg = UploadImage(imagem=request.FILES['resultado'])
            novaimg.save()
            converter.save(settings.BASE_DIR + '/app/' + novaimg.imagem.url)
            context = {'novaimg': novaimg}
            return render(request, 'app/resultado.html', context)

    else:
        form = ImagemForm()
        imagens = UploadImage.objects.all()

    return render(request, 'app/illuminantes.html', {'imagens': imagens, 'form': form})


def finish(request):
    return HttpResponseRedirect('/finish')



def resultado(request):
    return render(request,'app/resultado.html')

