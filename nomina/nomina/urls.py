from django.contrib import admin
from django.urls import path
from appnomina.views import inicio,crearCargo,editarCargo,eliminarCargo
from appnomina.views import crearDepartamento,editarDepartamento,eliminarDepartamento 
from appnomina.views import crearEmpleado,editarEmpleado,eliminarEmpleado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio" ),
    
    #se referencia la vista crearCargo al momento (cargo/)
    path('cargo/',crearCargo,name="cargo" ),
    path('editar_cargo/<int:id>',editarCargo,name="editar_cargo" ),
    path('eliminar_cargo/<int:id>',eliminarCargo,name="eliminar_cargo" ),
    
    
    #referencia la vista departamento
    path('dpto/',crearDepartamento,name="departamento" ),
    path('editar_departamento/<int:id>',editarDepartamento,name="editar_departamento"),
    path('eliminar_departamento/<int:id>',eliminarDepartamento, name='eliminar_departamento'),
    
    
    #referencia la vista empleado
    path('empleado/',crearEmpleado,name="empleado" ),
    path('editar_empleado/<int:id>',editarEmpleado,name="editar_empleado" ),
    path('eliminar_empleado/<int:id>',eliminarEmpleado,name="eliminar_empleado" ),
]
 