from django.shortcuts import redirect, render
from apps.post.forms import CustomUserCreationForm
from django.contrib.auth import views as auth
from django.contrib.auth.forms import UserCreationForm

from apps.post.models import categoria, post
from django.contrib.auth import authenticate, login
from django.contrib import messages

from apps.usuarios.models import Usuario


def EcoGreen(request):

	r = categoria.objects.all()

	ctx = {}
	ctx['categorias'] = r

	
	return render(request,'EcoGreen.html',ctx)
    
    
def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te registraste bien")
            return redirect(to="EcoGreen")
        data["form"] = formulario 
      
    return render(request, "usuarios/registro.html", data)



