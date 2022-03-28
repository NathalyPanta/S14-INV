from dataclasses import field
from tkinter import Widget 
from django import forms
from .models import Cargo, Departamento, Empleado

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese cargo',
                'class':'form-group',
                'required':True
            }),            
        }
     
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese Departamento',
                'class':'form-group',
                'required':True
            }),
        }
        

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','cedula','cargo','departamento','sueldo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder':'Ingrese su Nombre',
                'class':'form-group',
                'required':True,
                'size':50
            }),
            'cedula': forms.TextInput(attrs={
                'placeholder':'Ingrese su número de Cédula',
                'class':'form-group',
                'required':True,
                'size':50
            }),
            'cargo': forms.Select(attrs={
                'class':'form-group',
                'required':True
            }),
            'departamento': forms.Select(attrs={
                'class':'form-group',
                'required':True,
            }),
            'sueldo': forms.TextInput(attrs={
                'placeholder':'Ingrese su Sueldo',
                'class':'form-group',
                'required':True,
                'size':50,
            })
        }
        