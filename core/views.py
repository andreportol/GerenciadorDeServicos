from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from .models import ChamadoSuporte, Cliente, Funcionario

app_name = 'core'

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

class ClienteCreateView(CreateView):
    template_name = 'cadastrocliente.html'
    model = Cliente
    fields = '__all__'

class FuncionarioCreateView(CreateView):
    template_name = 'cadastrofuncionario.html'
    model = Funcionario
    fields = '__all__'

class ChamadoSuporteCreateView(CreateView):
   template_name = 'cadastrosuporte.html'
   model = ChamadoSuporte
   fields = '__all__' 
