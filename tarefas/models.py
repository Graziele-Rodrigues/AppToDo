from django.db import models

# Create your models here.
class Tarefa(models.Model):
    conteudo = models.CharField(max_length=100)
    data=models.DateTimeField(auto_now_add=True)
    completado=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
        