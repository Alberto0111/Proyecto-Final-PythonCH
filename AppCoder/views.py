#from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Usuario, Especialista, Planta, Comentario
from AppCoder.forms import PlantaForm, BusquedaPlantaForm, UsuarioForm, EspecialistaForm, ComentarioForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class PlantaList(LoginRequiredMixin ,ListView):
    model = Planta
    template_name = "AppCoder/plantas_1.html"

class PlantaDetalle(DetailView):
    model = Planta
    template_name = "AppCoder/planta_detalle.html"

class PlantaCreacion(LoginRequiredMixin ,CreateView):
    model = Planta
    success_url = "/app/plantas/listar"
    template_name = "AppCoder/crear_planta.html"
    fields = ["nombre_comun", "nombre_cientifico","imagen"]

class PlantaActualizacion(UpdateView):
    model = Planta
    success_url = "/app/plantas/listar"
    template_name = "AppCoder/crear_planta.html"
    fields = ["nombre_comun", "nombre_cientifico"]

class PlantaEliminar(DeleteView):
    model = Planta
    template_name = "AppCoder/eliminar.html"
    success_url = "/app/plantas/listar"

def home(request):
    return render (request, "AppCoder/home.html")

def comentario_planta(request, pk):
    planta = Planta.objects.get(pk=pk)
    comentarios = planta.comentarios.all()
    if request.method == "POST":
        form= ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.planta = planta
            comentario.save()
            return redirect ("Comentarios", pk=pk)
    else:
        form = ComentarioForm()
        contexto = {
            "planta":planta,
            "comentarios":comentarios,
            "form":form,
        }
        return render(request, "AppCoder/comentarios.html", contexto)
    
def sobre_mi(request):
    return render(request, "AppCoder/sobre_mi.html")

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
