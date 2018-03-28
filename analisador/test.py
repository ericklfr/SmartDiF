from django.conf import settings
import os
from analisador.models import Snippet
from analisador.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import Snippet

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")



snippet = Snippet(code='print "hello, world"\n')
snippet.save()