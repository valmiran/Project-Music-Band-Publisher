from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Artista, Projeto, Evento, Edital

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email') 
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.tipo:
            user.tipo = 'VISITANTE'
        if commit:
            user.save()
        return user

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['genero_musical', 'biografia', 'foto_perfil', 'instrumentos']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'genero_musical': forms.TextInput(attrs={'class': 'form-control'}),
            'instrumentos': forms.CheckboxSelectMultiple(),
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'status']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data', 'local', 'status', 'projeto']
        widgets = {
            'data': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'projeto': forms.Select(attrs={'class': 'form-select'}),
        }

class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = ['titulo', 'conteudo', 'arquivo_pdf', 'data_abertura', 'data_fechamento', 'ativo']
        widgets = {
            'data_abertura': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'data_fechamento': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo_pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

''' EXPLICAÇÃO SOBRE UsuarioCreationForm e UserCreationForm:
1º O que é UsuarioCreationForm?
    R: UsuarioCreationForm é uma classe personalizada que estende a funcionalidade do UserCreationForm do Django.
        Ela é usada para criar novos usuários no sistema, permitindo a inclusão de campos adicionais ou personalizações específicas
        para o modelo de usuário definido na aplicação.
        
2º O que é UserCreationForm?
    R: UserCreationForm é uma classe fornecida pelo Django que facilita a criação de novos usuários.
        Ela inclui campos padrão como nome de usuário, senha e confirmação de senha, além de validações básicas para garantir que os dados inseridos sejam válidos.
'''


''' EXPLICAÇÃO SOBRE O CODIGO ACIMA

1º No nosso caso, estamos criando um formulario de cadastro que já criptograda a senha do usuario e define o usuario como VISITANTE caso ele nao escolha um tipo.

'''