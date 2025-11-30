from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario, Artista

@receiver(post_save, sender=Usuario)
def gerenciar_perfil_artista(sender, instance, created, **kwargs):
    if instance.tipo in ['MEMBRO', 'PROFESSOR']:
        Artista.objects.get_or_create(usuario=instance)


    """
    # O método get_or_create garante que não duplicaremos se já existir
    Sempre que um usuário é criado ou salvo:
    1. Se for criado e o tipo for MEMBRO ou PROFESSOR, cria o perfil de Artista.
    2. Se for alterado de VISITANTE para MEMBRO/PROFESSOR, cria o perfil se não existir.
    """