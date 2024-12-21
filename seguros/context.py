from .models import Seguro, Plano, Empresa

def lista_seguros(request):
    lista_seguro = Seguro.objects.all()
    return {'lista_seguro': lista_seguro}

def lista_planos(request):
    lista_plano = Plano.objects.all()
    return {'lista_plano': lista_plano}

def lista_empresas(request):
    lista_empresa = Empresa.objects.all()
    return {'lista_empresa': lista_empresa}

def pesquisar_seguro(request):
    usuario_pesquisa = request.GET.get('q')
    if usuario_pesquisa:
        pesquisa_seguro = Seguro.objects.filter(titulo_seguro__icontains=usuario_pesquisa)
        pesquisa_plano = Plano.objects.filter(titulo_plano__icontains=usuario_pesquisa)
        return{'pesquisa_seguro': pesquisa_seguro, 'pesquisa_plano': pesquisa_plano}
    
    pesquisa_seguro = None
    pesquisa_plano = None
    return{'pesquisa_seguro': pesquisa_seguro, 'pesquisa_plano': pesquisa_plano}
