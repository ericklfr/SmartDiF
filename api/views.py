from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from api.serializers import SomarAPISerializer
from api.models import SomarAPI
from subprocess import PIPE
import subprocess
import json
import sys
from rest_framework.decorators import api_view

def SomarApiResultado(request):
    r = requests.get('http://localhost:8004/api/somarapi/2')
    serializer = SomarAPISerializer(r.json())
    total = subprocess.check_output([sys.executable, "somarscript.py -i %s %s", serializer['valor1'], serializer['valor2']])
    return render(request, 'analisador/resultado.html', {'resultado': total})

class SomarAPIViewSet(ModelViewSet):
    queryset = SomarAPI.objects.all()
    serializer_class = SomarAPISerializer

class SomarApiResultado(APIView):
    def get(self, request, pk, format=None):
        valores = self.get_object(pk);
        serializer = SomarAPISerializer(valores)
        total = subprocess.check_output([sys.executable, "somarscript.py -i %s %s", serializer['valor1'], serializer['valor2']])
        return render(request,'analisador/resultado.html',{'resultado':total})

class SomarApiList(APIView):
    def get(self, request):
        valores = SomarAPI.objects.all()
        serializer = SomarAPISerializer(valores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SomarAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(5+5)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def test(request):

    resultado = subprocess.check_output(args = ['python', 'api/somarscript.py', str(request.data.get("valor1")), str(request.data.get("valor2"))], shell = False)
    resultado = resultado
    #resultado = subprocess.check_call(['somarscript.py', str(request.data.get("valor1")), str(request.data.get("valor2"))])
    #resultado = subprocess.check_output([sys.executable, '/home/erick/myproject/myproject/api/somarscript.py','-i', str(request.data.get("valor1")), str(request.data.get("valor2"))])
    return Response(resultado)
