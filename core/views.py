from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UsuarioCreationForm, ArtistaForm, ProjetoForm, EventoForm
from .models import Artista, Projeto, Usuario, Evento

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
    artista = get_object_or_404(Artista, usuario=request.user)
    
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistaForm(instance=artista)
    
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def meu_perfil(request):
    artista = get_object_or_404(Artista, usuario=request.user)
    return render(request, 'perfil.html', {'artista': artista})

def is_professor(user):
    return user.is_authenticated and user.tipo == 'PROFESSOR'

def is_gestor_or_admin(user):
    return user.is_authenticated and (user.tipo == 'GESTOR' or user.tipo == 'ADMIN' or user.is_superuser)

def can_create_content(user):
    return user.is_authenticated and (user.tipo == 'PROFESSOR' or user.tipo == 'ADMIN' or user.is_superuser)

@login_required
def listar_projetos(request):
    projetos = Projeto.objects.all().order_by('-data_inicio')
    return render(request, 'projetos/lista.html', {'projetos': projetos})

@login_required
def listar_eventos(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'eventos/lista.html', {'eventos': eventos})

@user_passes_test(can_create_content) 
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.criado_por = request.user
            #projeto.aprovar() 
            projeto.save()
            messages.success(request, "Projeto criado com sucesso!")
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    
    return render(request, 'projetos/form.html', {'form': form, 'titulo': 'Novo Projeto'})

@user_passes_test(is_gestor_or_admin)
def gerenciar_equipe(request):
    usuarios = Usuario.objects.all().order_by('first_name')
    return render(request, 'gerenciar_equipe.html', {'usuarios': usuarios})

@user_passes_test(is_gestor_or_admin)
def alterar_cargo(request, user_id):
    if request.method == 'POST':
        usuario_alvo = get_object_or_404(Usuario, id=user_id)
        
        if usuario_alvo == request.user:
            messages.error(request, "Você não pode alterar seu próprio cargo por aqui.")
            return redirect('gerenciar_equipe')
        
        if usuario_alvo.is_superuser and not request.user.is_superuser:
            messages.error(request, "Você não tem permissão para alterar um Super Admin.")
            return redirect('gerenciar_equipe')

        novo_tipo = request.POST.get('novo_tipo')
        tipos_validos = dict(Usuario.TIPO_USUARIO).keys()

        if novo_tipo in tipos_validos:
            usuario_alvo.tipo = novo_tipo
            usuario_alvo.save()
            messages.success(request, f"Cargo de {usuario_alvo.username} alterado para {usuario_alvo.get_tipo_display()}.")
        else:
            messages.error(request, "Tipo de usuário inválido.")
            
    return redirect('gerenciar_equipe')

@user_passes_test(can_create_content) 
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criado_por = request.user
            #evento.aprovar() 
            evento.save()
            messages.success(request, "Evento agendado com sucesso!")
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    
    return render(request, 'eventos/form.html', {'form': form, 'titulo': 'Agendar Novo Evento'})

@user_passes_test(can_create_content)
def editar_evento(request, event_id):
    evento = get_object_or_404(Evento, id=event_id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento atualizado com sucesso!")
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'eventos/form.html', {'form': form, 'titulo': 'Editar Evento'})

@user_passes_test(can_create_content) 
def editar_projeto(request, project_id):
    projeto = get_object_or_404(Projeto, id=project_id)
    
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, "Projeto atualizado com sucesso!")
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    
    return render(request, 'projetos/form.html', {'form': form, 'titulo': 'Editar Projeto'})


@user_passes_test(can_create_content)
def excluir_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    
    projeto.delete()
    
    messages.success(request, "Projeto excluído com sucesso!")
    return redirect('listar_projetos')

@user_passes_test(can_create_content)
def excluir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    
    evento.delete()
    
    messages.success(request, "Evento excluído com sucesso!")
    return redirect('listar_eventos')

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
