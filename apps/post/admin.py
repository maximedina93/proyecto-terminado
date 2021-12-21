from django.contrib import admin
from apps import post
from apps.usuarios.models import Usuario
from .models import categoria, post
from django.contrib import admin

admin.site.register(categoria)
admin.site.register(post)
admin.site.register(Usuario)
