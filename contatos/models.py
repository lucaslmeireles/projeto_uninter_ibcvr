from django.utils import timezone
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=55, verbose_name='nome_categoria', blank=True, null=True)
    def __str__(self) -> str:
        return self.nome_cat

class Contato(models.Model):
    nome = models.CharField(max_length=255, verbose_name='nome')
    sobrenome = models.CharField(max_length=255, verbose_name='sobrenome')
    telefone = models.CharField(max_length=14, verbose_name='telefone')
    data_nascimento = models.DateField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    email = models.EmailField(verbose_name='email', blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome