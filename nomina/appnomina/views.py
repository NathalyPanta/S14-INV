from django.shortcuts import redirect,render,HttpResponse
from appnomina.forms import CargoForm,DepartamentoForm,EmpleadoForm
from .models import Cargo, Empleado, Departamento

# Create your views here. 

def inicio(request):
    #return HttpResponse("<h1>Bienvenido a mi Sitio Web</h1>")
    return render(request, "inicio.html")

##################################################################

#Crea Vista para crear cargo
def crearCargo(request):
    #metodo post
    if request.method == "POST":
        print("entro por post")
        #instancio un objeto de tipo formulario cargo
        cargo_form =CargoForm(request.POST)
        #verifica si los datos son validos
        if cargo_form.is_valid():
            #se guarda el cambio
            cargo_form.save()
    else:
        print("entro por get")
        #se instancia un objeto de tipo cargo
    cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render (request, "pages/cargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion':'Crear'})

#vista para modificar
def editarCargo(request,id):
    error,cargo_form=None,None
    try:
        cargo = Cargo.objects.get(id=id)
        if request.method == "GET":
            cargo_form = CargoForm(instance=cargo)
        else:
            cargo_form = CargoForm(request.POST,instance=cargo)
            if cargo_form.is_valid():
                #se guardan los cambios (lo que se ha modificado)
                cargo_form.save()
                #se catualiza la pág
                return redirect('cargo')
    except Exception as e:
        error=e
    #se traen los datos
    # cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render (request, "pages/cargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion':'Actualizar'})

def eliminarCargo (request,id):
    cargo = Cargo.objects.get(id=id)
    if request.method == 'POST':
        cargo.delete()
        return redirect ("cargo")
    return render (request,'pages/eliminar_cargo.html',{'cargo':cargo})
 
 
#/////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
       
#Vista para Departamento
def crearDepartamento(request):
    #metodo POST
    if request.method == "POST":
        print("entró por post ")
        #se instancia un objeto tipo formulario
        departamento_form = DepartamentoForm(request.POST)
        #se verifica que los datos sean validos (is.valid)
        if departamento_form.is_valid():
            #se guarda
            departamento_form.save()
    else:
        print("entró por get ")
        
        #se traen los departamentos
    departamento_form = DepartamentoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.html", {'departamentoForm':departamento_form, 'departamentos':departamentos, 'accion':'Crear'})

#vista para modificar
def editarDepartamento(request,id):
    error,departamento_form=None,None
    try:
        departamento = Departamento.objects.get(id=id)
        if request.method == "GET":
            departamento_form = DepartamentoForm(instance=departamento)
        else:
            departamento_form = DepartamentoForm(request.POST,instance=departamento)
            if departamento_form.is_valid():
                #se guardan los cambios (lo que se ha modificado)
                departamento_form.save()
                #se catualiza la pág
                return redirect('departamento')
    except Exception as e:
        error=e
    #se traen los datos
    # departamento_form = DepartamentoForm()
    departamentos = Departamento.objects.all()
    return render (request, "pages/departamento.html",{'departamentoForm':departamento_form,'departamentos':departamentos,'accion':'Actualizar'})

#vista para eliminar
def eliminarDepartamento(request,id):
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
        #eliminación física del registro
        departamento.delete()
        return redirect ("departamento")
    return render (request,'pages/eliminar_departamento.html',{'departamento':departamento})


##################################################################


def crearEmpleado(request):
    # print(request)
    # print(request.method)
    if request.method == "POST":
        print("entró por post")
        empleado_form = EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
    else:
        print("entró por get")
    empleado_form = EmpleadoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.html",{'empleadoForm': empleado_form,'empleados':empleados,'accion':'Crear'})
    
def editarEmpleado (request,id):
    error,empleado_form =None,None
    try:
        empleado = Empleado.objects.get(id=id)
        if request.method == "GET":
            empleado_form=EmpleadoForm(instance=empleado)
        else:
            empleado_form=EmpleadoForm(request.POST, instance=empleado)
            if empleado_form.is_valid():
                empleado_form.save()
                return redirect ('empleado')
    except Exception as e:
        error = e
    empleados = Empleado.objects.all()
    return render (request, "pages/empleado.html",{'empleadoForm':empleado_form,'empleados':empleados,'accion':'Actualizar'})

def eliminarEmpleado(request,id):
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect("empleado")
    return render (request, 'pages/eliminar_empleado.html',{'empleado':empleado})

            
            