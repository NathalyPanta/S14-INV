from operator import truediv
from pyexpat import model
from tabnanny import verbose
from django.db import models
from setuptools import Require 

# modelo cargo
class Cargo(models.Model):
    #campos
    descripcion = models.CharField(max_length=100, blank=False, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True) 
   
    #clase meta
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['id']
    def __str__(self):
        return self.descripcion

# modelo departamento
class Departamento(models.Model):
    #campos
    descripcion = models.CharField(max_length=100, blank=False, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
    #clase meta
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['id']
    def __str__(self):
        return self.descripcion
     
# modelo Empleado
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    cedula = models.CharField(max_length=10,blank=False,null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField (default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True) 
    
      #clase meta
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['-nombre']
    def __str__(self):
        return self.nombre
