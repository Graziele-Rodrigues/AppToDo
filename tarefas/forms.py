from django import forms
from .models import Tarefa

class ConteudoForm(forms.ModelForm):
    class Meta:
       model = Tarefa
       fields='__all__'