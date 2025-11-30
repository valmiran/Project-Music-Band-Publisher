from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UsuarioCreationForm

def home(request):
    return render(request, 'index.html')

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
'''
