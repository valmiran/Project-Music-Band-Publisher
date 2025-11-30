from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.meu_perfil, name='meu_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'), 
]