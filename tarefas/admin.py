from tarefas.models import Tarefa
from django.contrib import admin

# Register your models here.
class TarefaAdmin(admin.ModelAdmin):
    list_display=['id', 'conteudo', 'data',]

admin.site.register(Tarefa, TarefaAdmin)
