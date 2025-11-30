from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
1º      Quando adicionamos django.contrib.auth.urls, estamos incluindo um conjunto de URLs(Rotas) pré-definidas pelo Django para lidar com autenticação de usuários.
    Essas URLs fornecem funcionalidades essenciais, como login, logout e gerenciamento de senhas, sem a necessidade de criarmos essas rotas manualmente.

2º      Oque tem dentro de django.contrib.auth.urls?
    Aqui estão algumas das principais rotas incluídas quando usamos django.contrib.auth.urls:

    - login/ : Rota para a página de login, onde os usuários podem inserir suas credenciais para acessar o sistema.
    - logout/ : Rota para fazer logout do sistema, encerrando a sessão do usuário.
    - password_change/ : Rota para permitir que os usuários alterem suas senhas enquanto estão logados.
    - password_change/done/ : Rota que confirma que a senha foi alterada com sucesso.
    - password_reset/ : Rota para iniciar o processo de redefinição de senha, onde os usuários podem solicitar um link de redefinição.
    - password_reset/done/ : Rota que confirma que o pedido de redefinição de senha foi enviado.
    - reset/<uidb64>/<token>/ : Rota para redefinir a senha usando o link enviado por e-mail.
    - reset/done/ : Rota que confirma que a senha foi redefinida com sucesso.    
'''