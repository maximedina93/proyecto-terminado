from django.urls import path
from . import views 

app_name = 'post'

urlpatterns = [
 	
	path('listar/', views.listar_post, name = 'listar_post'),

	path('detalle/<int:pk>', views.DetallePost, name= 'detalle'),

	path('FILTRO/<int:pk>', views.FiltroXCategoria, name= 'filtro'),

	path('Alta/', views.altaPost.as_view(), name="alta_post"),
 
	path('noti/', views.noticias, name = 'noticias'),
 
	path('info/', views.informacion, name = 'informacion'),

	path('ods/', views.ods, name = 'ods'),

 
 
	


	path('noticiaslistar/', views.noticias_listar, name = 'noticias_listar'),
	

]
