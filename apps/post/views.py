from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import post, categoria
from .forms import  Formulario_alta_post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def listar_post(request):
	
	#CONSULTA PARA TRAER TODOS LOS PRODUCTOS
	# P QUERYSET (MUY PAECIDO A UN DICCIONARIO) QUE CONTIENE TODOS LOS PRODUCTOS QUE ESTEN EN LA BD
	p = post.objects.all()

	#CONTEXTO
	ctx = {}
	ctx['post'] = p
	ctx['titulo'] = "HOLA SOY EL TITULO"

	return render(request,'post/listar_post.html',ctx)
# EN REALIDAD EN EL TEMPLATE VOY TENER VARIABLES SEPARADAS

# pruduct QUE CONTIENE a p
# titulo


def DetallePost(request, pk):

	p = post.objects.get(pk = pk)

	ctx = {}
	ctx['post'] = p


	return render(request, 'post/detallePost.html',ctx)

@login_required
def FiltroXCategoria(request, pk):

	#TRAE SOLO LA CATEGORIA CON ESA PK
	Categoria = categoria.objects.get(pk = pk)
	#BUSCA TODOS LOS PRODUCTOS CON UNA RELACION A ESE CATEGORIA
	p = post.objects.filter(categoria = categoria )

	ctx = {}
	ctx['post'] = p
	ctx['categoria'] = categoria

	return render(request, 'post/filtroxCategoria.html',ctx)


class altaPost(LoginRequiredMixin, CreateView):
	model = 'post'
	template_name = 'post/alta.html'
	form_class = Formulario_alta_post
	success_url = reverse_lazy('post:listar_post')
 
 
@login_required
def noticias(request):
    	
	#CONSULTA PARA TRAER TODOS LOS PRODUCTOS
	# P QUERYSET (MUY PAECIDO A UN DICCIONARIO) QUE CONTIENE TODOS LOS PRODUCTOS QUE ESTEN EN LA BD
	p = post.objects.all()

	#CONTEXTO
	ctx = {}
	ctx['post'] = p
	ctx['titulo'] = "HOLA SOY EL TITULO"

	return render(request,'post/noticias.html',ctx)
 


@login_required
def noticias_listar(request):
	
	#CONSULTA PARA TRAER TODOS LOS PRODUCTOS
	# P QUERYSET (MUY PAECIDO A UN DICCIONARIO) QUE CONTIENE TODOS LOS PRODUCTOS QUE ESTEN EN LA BD
	p = post.objects.all()

	#CONTEXTO
	ctx = {}
	ctx['post'] = p
	ctx['noticias'] = "NOTICIAS AMBIENTALES"

	return render(request,'post/noticias_listar.html',ctx)



@login_required
def informacion(request):
	
	#CONSULTA PARA TRAER TODOS LOS PRODUCTOS
	# P QUERYSET (MUY PAECIDO A UN DICCIONARIO) QUE CONTIENE TODOS LOS PRODUCTOS QUE ESTEN EN LA BD
	p = post.objects.all()

	#CONTEXTO
	ctx = {}
	ctx['post'] = p
	ctx['informacion'] = "INFO"

	return render(request,'post/informacion.html',ctx)


@login_required
def ods(request):
	
	#CONSULTA PARA TRAER TODOS LOS PRODUCTOS
	# P QUERYSET (MUY PAECIDO A UN DICCIONARIO) QUE CONTIENE TODOS LOS PRODUCTOS QUE ESTEN EN LA BD
	p = post.objects.all()

	#CONTEXTO
	ctx = {}
	ctx['post'] = p
	ctx['ods'] = "ods"

	return render(request,'post/ods.html',ctx)





