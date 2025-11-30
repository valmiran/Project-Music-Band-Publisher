from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.meu_perfil, name='meu_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'), 
    
    path('equipe/', views.gerenciar_equipe, name='gerenciar_equipe'),
    path('equipe/alterar-cargo/<int:user_id>/', views.alterar_cargo, name='alterar_cargo'),

    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/novo/', views.criar_evento, name='criar_evento'),
    path('eventos/editar/<int:event_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/excluir/<int:id>', views.excluir_evento, name='excluir_evento'),

    path('projetos/', views.listar_projetos, name='listar_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/editar/<int:project_id>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/excluir/<int:id>', views.excluir_projeto, name='excluir_projeto'),
]