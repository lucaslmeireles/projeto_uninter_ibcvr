from django.contrib import admin
from .models import Contato, Categoria
# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
     list_display = ('nome', 'sobrenome', 'telefone', 'email', 'data_nascimento', 'categoria')
     list_editable = ('email', 'telefone',)
     search_fields = ('nome', 'telefone',)


admin.site.register(admin_class=ContatoAdmin,model_or_iterable=Contato)
admin.site.register(Categoria)