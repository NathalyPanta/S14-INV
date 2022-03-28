from django.contrib import admin
from .models import Cargo, Empleado, Departamento

#añadir los modelos al administrador
# Register your models here.

admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)
