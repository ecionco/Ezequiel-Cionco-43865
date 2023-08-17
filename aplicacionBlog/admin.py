from django.contrib import admin
from .models import Trabajo, Trabajador, Vinculacion, Recomendacion, Avatar
# Register your models here.

admin.site.register(Trabajo)
admin.site.register(Trabajador)
admin.site.register(Vinculacion)
admin.site.register(Recomendacion)
admin.site.register(Avatar)