from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UsuarioCreationForm,ArtistaForm
from .models import Artista

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required # Só quem está logado acessa
def editar_perfil(request):
    # Tenta pegar o perfil do artista. Se não existir (ex: é só Visitante), dá erro 404.
    artista = get_object_or_404(Artista, usuario=request.user)
    
    if request.method == 'POST':
        # request.FILES é obrigatório para salvar a foto!
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('home') # Ou redirecionar para uma página de "Meu Perfil"
    else:
        form = ArtistaForm(instance=artista)
    
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def meu_perfil(request):
    # Busca o artista logado. Se não tiver perfil (ex: Visitante), dá erro 404
    artista = get_object_or_404(Artista, usuario=request.user)
    return render(request, 'perfil.html', {'artista': artista})


"""Resumo Técnico das Views"""

''' 
    home(request)
    Propósito: Renderizar a página inicial da aplicação.

    Funcionamento:

    Recebe uma requisição HTTP
    Retorna o template index.html renderizado ao cliente
    Não requer autenticação ou processamento de dados
    Tipo: View simples de apresenta

    ===============================================================================

    cadastro(request)
    Propósito: Gerenciar o registro de novos usuários no sistema.

    Funcionamento:

    GET: Exibe formulário vazio (UsuarioCreationForm) na página de cadastro
    POST: Processa dados do formulário enviados pelo usuário
    Valida os dados com form.is_valid()
    Se válido: salva o usuário no banco de dados com form.save()
    Autentica automaticamente o usuário com login(request, user)
    Redireciona para a página inicial (home)
    Se inválido: reexibe o formulário com mensagens de erro
    Tipo: View de processamento de formulário com autenticação automática

    Template utilizado: registration/cadastro.html

    Dependências: UsuarioCreationForm (formulário customizado de criação de usuário)

    ==================================================================================

    editar_perfil(request)
    Propósito: Permitir que usuários autenticados editem seu perfil de artista.

    Funcionamento:

    Autenticação obrigatória: Usa decorador @login_required (redireciona para login se não autenticado)
    Busca o perfil do artista associado ao usuário logado com get_object_or_404()
    Retorna erro 404 se o usuário não tiver um perfil de artista
    GET: Exibe formulário (ArtistaForm) preenchido com dados atuais do artista
    POST: Processa dados do formulário incluindo arquivo de imagem
    Valida os dados com form.is_valid()
    Se válido: salva as alterações no banco de dados com form.save()
    Redireciona para a página inicial
    Se inválido: reexibe o formulário com mensagens de erro
    Tipo: View de edição com autenticação obrigatória e processamento de upload de arquivos

    Template utilizado: editar_perfil.html

    Dependências: ArtistaForm (formulário de edição do perfil de artista), modelo Artista
'''
