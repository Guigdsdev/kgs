from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, TemplateView, DetailView, FormView
from .models import Seguro, Contato, Plano
from .forms import FormContato
from send_email import sendEmail
# Create your views here.

class HomePage(ListView):
    template_name = 'homepage.html'
    model = Seguro

class DetalheSeguro(DetailView, FormView):
    template_name = 'detalheseguros.html'
    form_class = FormContato
    model = Seguro

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']

        servico = self.get_object()
        servico.titulo_seguro

        # contato = Contato(nome=nome, email=email, telefone=telefone)
        sendEmail(nome=nome, mail=email,servico=servico, numero=telefone)

        # contato.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Você preencheu alguma informação incorreta.")
        # Renderiza a página novamente com o formulário inválido e `self.object` definido
        self.object = self.get_object()  # Garante que `self.object` está configurado
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        messages.success(self.request, 'Contato enviado com sucesso')
        return reverse('seguros:homepage')
           
class DetalhePlano(DetailView, FormView):
    template_name = 'detalheplanos.html'
    model = Plano
    form_class  = FormContato

    def get_object(self, queryset = None):
        return super().get_object(queryset)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']

        servico = self.get_object()
        servico.titulo_plano
        
        #contato = Contato(nome=nome, email=email, telefone=telefone)
        sendEmail(nome=nome, mail=email,servico=servico, numero=telefone)

        #contato.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Você preencheu alguma informação incorreta.")
        # Renderiza a página novamente com o formulário inválido e `self.object` definido
        self.object = self.get_object()  # Garante que `self.object` está configurado
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        messages.success(self.request, 'Contato enviado com sucesso')
        return reverse('seguros:homepage')

class ContatoPagina(FormView):
    template_name = 'contato.html'
    form_class = FormContato

    def get_success_url(self):
        nome = self.request.POST.get('nome')
        email = self.request.POST.get('email')
        telefone = self.request.POST.get('telefone')

        servico = 'Entre em contato comigo'

        #contato = Contato(nome=nome, email=email, telefone=telefone)
        sendEmail(nome=nome, mail=email,servico=servico, numero=telefone)

        messages.success(self.request, 'Contato enviado com sucesso')

        #contato.save()
        return reverse('seguros:homepage')
    
    def form_invalid(self, form):
        messages.error(self.request, "Você preencheu alguma informação incorreta.")
        return super().form_invalid(form)

class Pesquisador(TemplateView):
    template_name = 'pesquisador.html'

class SeguroDeVida(TemplateView):
    template_name = 'segurodevida.html'
    
class SeguroViagem(TemplateView):
    template_name = 'seguroviagem.html'


class Odonto(TemplateView):
    template_name = 'odonto.html'

class Doctor(TemplateView):
    template_name = 'doctor.html'

class Sobre(TemplateView):
    template_name = 'sobrenos.html'


