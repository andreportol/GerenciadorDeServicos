from django.db import models


# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=50, unique=True)

class Funcionario(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=50)

class ChamadoSuporte(models.Model):
    numero = models.IntegerField(verbose_name='Número do Chamado')
    cliente_id = models.ForeignKey(Cliente, to_field= 'nome', verbose_name='Nome do Cliente', on_delete=models.PROTECT)