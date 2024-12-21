from django.urls import path
from .views import HomePage, SeguroDeVida, SeguroViagem, Odonto, Doctor, DetalheSeguro, DetalhePlano, ContatoPagina, Sobre, Pesquisador

app_name = 'seguros'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('seguro/<int:pk>/', DetalheSeguro.as_view(), name='detalheseguros'),
    path('plano/<int:pk>/', DetalhePlano.as_view(), name='detalheplanos'),
    path('pesquisa/', Pesquisador.as_view(), name='pesquisa'),
    path('sobrenos/', Sobre.as_view(), name='sobrenos'),
    path('segurodevida/', SeguroDeVida.as_view(), name="segurodevida"),
    path('seguroviagem/', SeguroViagem.as_view(), name='seguroviagem'),
    path('odonto/', Odonto.as_view(), name="odonto"),
    path('doctor/', Doctor.as_view(), name='doctor'),
    path('contato/', ContatoPagina.as_view(), name='contato'),
]
