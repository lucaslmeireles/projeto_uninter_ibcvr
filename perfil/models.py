from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=255, verbose_name='nome')
    sobrenome = models.CharField(max_length=255, verbose_name='sobrenome')
    telefone = models.CharField(max_length=14, verbose_name='telefone')
    data_nascimento = models.DateField(default=timezone.now)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    email = models.EmailField(verbose_name='email')
    