from django import forms

from apps import post
from apps.usuarios.models import Usuario

from .models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Formulario_alta_post(forms.ModelForm):
	

	class Meta:
		model = post
		fields = '__all__'
  
  
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1','password2']
      
