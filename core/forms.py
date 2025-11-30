from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Artista

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
            'biografia': forms.Textarea(attrs={'rows': 3}),
            'instrumentos': forms.CheckboxSelectMultiple(), # Checkbox fica melhor para escolher vários
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