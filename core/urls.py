from django.urls import path

from core.views import (ChamadoSuporteCreateView, ClienteCreateView,
                        FuncionarioCreateView, IndexTemplateView)

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('cadastrar_cliente/', ClienteCreateView.as_view(), name='cadastrar_cliente'),
    path('cadastrar_chamado/', ChamadoSuporteCreateView.as_view(), name='cadastrar_chamado'),
    path('cadastrar_funcionario/', FuncionarioCreateView.as_view(), name='cadastrar_funcionario'),
]
