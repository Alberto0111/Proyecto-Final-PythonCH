#from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Usuario, Especialista, Planta
from AppCoder.forms import PlantaForm, BusquedaPlantaForm, UsuarioForm, EspecialistaForm

def mostrar_plantas(request):
    plantas = Planta.objects.all()
    contexto = {
        "plantas": plantas,
        "form": BusquedaPlantaForm(),
    }
    return render(request, 'AppCoder/plantas.html', contexto)

def crear_planta_form(request):
    if request.method == "POST":
        planta_formulario = PlantaForm(request.POST)
        if planta_formulario.is_valid():
            informacion = planta_formulario.cleaned_data
            planta_crear = Planta(nombre_comun = informacion["nombre_comun"], nombre_cientifico = informacion["nombre_cientifico"])
            planta_crear.save()
            return redirect("/app/plantas/")

    planta_formulario = PlantaForm()
    contexto = {
        "form": planta_formulario
    }
    return render(request, "AppCoder/crear_planta.html", contexto)

def busqueda_planta(request):
    nombre_comun = request.GET["nombre_comun"]
    plantas = Planta.objects.filter(nombre_comun__icontains=nombre_comun)
    contexto = {
        "plantas": plantas,
        "form": BusquedaPlantaForm(),
    }
    return render(request, 'AppCoder/plantas.html', contexto)

def crear_usuario_form(request):
    if request.method == "POST":
        usuario_formulario = UsuarioForm(request.POST)
        if usuario_formulario.is_valid():
            informacion = usuario_formulario.cleaned_data
            usuario_crear = Usuario(nombre = informacion["nombre"], apellido = informacion["apellido"])
            usuario_crear.save()
            return redirect("/app/plantas/")

    usuario_formulario = UsuarioForm()
    contexto = {
        "form": usuario_formulario
    }
    return render(request, "AppCoder/crear_usuario.html", contexto)

def crear_especialista_form(request):
    if request.method == "POST":
        especialista_formulario = EspecialistaForm(request.POST)
        if especialista_formulario.is_valid():
            informacion = especialista_formulario.cleaned_data
            especialista_crear = Especialista(nombre = informacion["nombre"], apellido = informacion["apellido"], email = informacion["email"])
            especialista_crear.save()
            return redirect("/app/plantas/")

    especialista_formulario = EspecialistaForm()
    contexto = {
        "form": especialista_formulario
    }
    return render(request, "AppCoder/crear_especialista.html", contexto)
