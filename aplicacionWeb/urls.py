from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    
    path('contacto/', contacto, name="contacto"),
    path('sobremi/', sobremi, name="sobremi"),
    path('noticia1/', noticia1, name="noticia1"),
    path('noticia2/', noticia2, name="noticia2"),
    path('noticia3/', noticia3, name="noticia3"),
    path('noticia4/', noticia4, name="noticia4"),
    ]
