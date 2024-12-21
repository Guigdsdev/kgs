from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Seguro(models.Model):
    titulo_seguro = models.CharField(max_length=100)
    img_seguro = models.ImageField(upload_to='seguros/', default='default.jpg')
    descricao_seguro = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo_seguro

class Plano(models.Model):
    titulo_plano = models.CharField(max_length=100)
    img_plano = models.ImageField(upload_to='planos/', default='default.jpg')
    descricao_plano = models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo_plano

class Empresa(models.Model):
    titulo_empresa = models.CharField(max_length=100)
    img_empresa = models.ImageField(upload_to='empresas/', default='default.jpg')

    def __str__(self):
        return self.titulo_empresa

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = PhoneNumberField(blank=True)
