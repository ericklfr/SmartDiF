from django.contrib import admin
from .models import audio,imagem,video,texto,outros

admin.site.register(imagem)
admin.site.register(video)
admin.site.register(audio)
admin.site.register(texto)
admin.site.register(outros)


