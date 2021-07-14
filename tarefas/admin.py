from tarefas.models import Tarefa
from django.contrib import admin

# Register your models here.
admin.site.register(Tarefa)

class TarefaAdmin(admin.ModelAdmin):
    list_display=['id', 'conteudo', 'data',]