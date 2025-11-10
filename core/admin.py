from django.contrib import admin
from .models import Usuario, Projeto, Evento, Artista, Instrumento, Notificacao, Atualizacao

admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Evento)
admin.site.register(Artista)
admin.site.register(Instrumento)
admin.site.register(Notificacao)
admin.site.register(Atualizacao)