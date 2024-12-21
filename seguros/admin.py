from django.contrib import admin
from .models import Seguro, Plano, Empresa
# Register your models here.
admin.site.register(Seguro)
admin.site.register(Plano)
admin.site.register(Empresa)
