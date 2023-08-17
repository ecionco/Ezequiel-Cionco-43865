from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', index, name="home"),
    
    
    path('post/', post, name="post"),
    path('vinculaciones/', vinculacion, name="vinculaciones"),
    
        
    path('buscar_habilidades/', buscarHabilidades, name="buscar_habilidades"),
    path('buscar_habilidades2/', buscarHabilidades2, name="buscar_habilidades2"),
    
    path('buscar_titulo/', buscarTitulo, name="buscar_titulo"),
    path('buscar_titulo2/', buscarTitulo2, name="buscar_titulo2"),
    
    path('buscar_rubro/', buscarRubro, name="buscar_rubro"),
    path('buscar_rubro2/', buscarRubro2, name="buscar_rubro2"),
    
    path('buscar_nombre/', buscarNombre, name="buscar_nombre"),
    path('buscar_nombre2/', buscarNombre2, name="buscar_nombre2"),
    
    path('buscar_trabajador/', buscarTrabajador, name="buscar_trabajador"),
    path('buscar_trabajador2/', buscarTrabajador2, name="buscar_trabajador2"),
    
    
        
    path('recomendaciones/', RecomendacionList.as_view(), name="recomendaciones"),
    path('create_recomendacion/', RecomendacionCreate.as_view(), name="create_recomendacion"),
    path('detail_recomendacion/<int:pk>/', RecomendacionDetail.as_view(), name="detail_recomendaciones"),
    path('update_recomendacion/<int:pk>/', RecomendacionUpdate.as_view(), name="update_recomendaciones"),
    path('delete_recomendacion/<int:pk>/', RecomendacionDelete.as_view(), name="delete_recomendaciones"),
    
    path('trabajo/', TrabajoList.as_view(), name="trabajo"),
    path('create_trabajo/', TrabajoCreate.as_view(), name="create_trabajo"),
    path('detail_trabajo/<int:pk>/', TrabajoDetail.as_view(), name="detail_trabajos"),
    path('delete_trabajo/<int:pk>/', TrabajoDelete.as_view(), name="delete_trabajos"),
    path('update_trabajo/<int:pk>/', TrabajoUpdate.as_view(), name="update_trabajos"),
    
    path('trabajador/', TrabajadorList.as_view(), name="trabajador"),
    path('create_trabajador/', TrabajadorCreate.as_view(), name="create_trabajador"),
    path('detail_trabajador/<int:pk>/', TrabajadorDetail.as_view(), name="detail_trabajadores"),
    path('delete_trabajador/<int:pk>/', TrabajadorDelete.as_view(), name="delete_trabajadores"),
    path('update_trabajador/<int:pk>/', TrabajadorUpdate.as_view(), name="update_trabajadores"),
    
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacionBlog/logout.html"), name="logout"),
    path('register/', register, name="register"),
    
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    ]
