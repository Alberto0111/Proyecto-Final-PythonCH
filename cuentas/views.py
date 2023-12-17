from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from cuentas.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from cuentas.models import Avatar
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            contrasenia = data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user:
                login(request, user)
                return redirect('PlantasList')            
        else:
            messages.error(request, "Usuario o contraseña incorrectos, por favor intenta nuevamente.", extra_tags='danger')  
    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "cuentas/login.html", contexto)

def register_request(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("PlantasList") 
        
    #form = UserCreationForm()
    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request,"cuentas/registro.html", contexto)

@login_required
def editar_request(request):
    user = request.user
    if request.method == "POST":
        user.email = request.POST["email"]
        user.save()
        return redirect("PlantasList")

    form = UserUpdateForm(initial={"username": user.username, "email": user.email})
    contexto = {
        "form": form
    }
    return render(request, "cuentas/registro.html", contexto)

@login_required
def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user= user,
                    imagen = data["imagen"]
                )
            avatar.save()
            return redirect("PlantasList")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "cuentas/avatar.html", contexto)

def mi_perfil(request):
    return render(request, "cuentas/perfil.html")