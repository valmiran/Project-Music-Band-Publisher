from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('ADMIN', 'Super Admin'),
        ('GESTOR', 'Gestor'),          
        ('PROFESSOR', 'Professor'), 
        ('MEMBRO', 'Membro da Banda'), 
        ('VISITANTE', 'Visitante'),

    ]
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO, default='VISITANTE')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="usuario_set", 
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_set", 
        related_query_name="usuario",
    )

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"
    
    @property
    def is_gestor(self):
        return self.tipo == 'GESTOR' or self.tipo == 'ADMIN' or self.is_superuser
    
class Instrumento(models.Model):
    TIPO_INSTRUMENTO = [
        ('CORDA', 'Corda'),
        ('SOPRO', 'Sopro'),
        ('PERCUSSAO', 'Percussão'),
        ('TECLA', 'Tecla'),
        ('OUTRO', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_INSTRUMENTO)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"


class Artista(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    genero_musical = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    instrumentos = models.ManyToManyField(Instrumento, blank=True)

    def __str__(self):
        return self.usuario.username

class Projeto(models.Model):
    STATUS_PROJETO = [
        ('ANDAMENTO', 'Em andamento'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_PROJETO, default='ANDAMENTO')
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='projetos_criados')

    is_public = models.BooleanField(default=False, verbose_name="Público?")
    pending_approval = models.BooleanField(default=True, verbose_name="Pendente de Aprovação?")

    def aprovar(self):
        self.is_public = True
        self.pending_approval = False
        self.save()

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    STATUS_EVENTO = [
        ('PLANEJADO', 'Planejado'),
        ('REALIZADO', 'Realizado'),
        ('CANCELADO', 'Cancelado'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_EVENTO, default='PLANEJADO')
    projeto = models.ForeignKey(Projeto, on_delete=models.SET_NULL, null=True, blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='eventos_criados')

    is_public = models.BooleanField(default=False, verbose_name="Público?")
    pending_approval = models.BooleanField(default=True, verbose_name="Pendente de Aprovação?")

    def aprovar(self):
        self.is_public = True
        self.pending_approval = False
        self.save()

    def __str__(self):
        return self.titulo

class Atualizacao(models.Model):
    descricao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    referencia = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Atualização em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

class Notificacao(models.Model):
    mensagem = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario_destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notificacoes')
    visualizada = models.BooleanField(default=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Notificação para {self.usuario_destinatario.username}"
    
class Edital(models.Model):
    titulo = models.CharField(max_length=200, default="Edital de Seleção")
    conteudo = models.TextField()
    arquivo_pdf = models.FileField(upload_to='editais/', null=True, blank=True) # Requer Pillow instalado
    data_abertura = models.DateTimeField()
    data_fechamento = models.DateTimeField()
    ativo = models.BooleanField(default=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE, related_name='inscricoes')
    candidato = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mensagem = models.TextField()
    video_demonstracao = models.URLField(blank=True, null=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('PENDENTE', 'Pendente'), ('APROVADO', 'Aprovado')], default='PENDENTE')

    def __str__(self):
        return f"Inscrição: {self.candidato}"