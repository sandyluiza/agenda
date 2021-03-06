from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Criando tabelas com models

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # esse campo tem no máximo 100 caracteres
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')  # verbose_name é para colocar o nome do jeito que
    # quer que apareça no django
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # para exigir que a tabela se chame evento (ou outro nome que quiser)
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %Hh%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False