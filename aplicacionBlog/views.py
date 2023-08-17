from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy

from aplicacionBlog.forms import *
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "aplicacionBlog/base.html")

def post(request):
    return render(request, "aplicacionBlog/post.html")

@login_required
def trabajo(request):
    ctx = {"trabajos": Trabajo.objects.all()}
    return render(request, "aplicacionBlog/trabajos.html", ctx)

@login_required
def trabajadores(request):
    ctx = {"trabajador": Trabajador.objects.all()}
    return render(request, "aplicacionBlog/trabajador.html", ctx)

@login_required
def vinculacion(request):
    ctx = {"vinculaciones": Vinculacion.objects.all()}
    return render(request, "aplicacionBlog/vinculaciones.html", ctx)

@login_required
def recomendaciones(request):
    ctx = {"recomendaciones": Recomendacion.objects.all()}
    return render(request, "aplicacionBlog/recomendaciones.html", ctx)





@login_required
def buscarTitulo(request):
    return render(request, "aplicacionBlog/buscarTitulo.html")

@login_required
def buscarTitulo2(request):
    if request.GET ['titulo']:
        titulo = request.GET['titulo']
        trabajos = Trabajo.objects.filter(titulo__icontains=titulo)
        return render(request, "aplicacionBlog/resultadosTitulos.html", {"titulo": titulo, "trabajos": trabajos})
    return HttpResponse("No fueron ingresados datos")  

@login_required
def buscarRubro(request):
    return render(request, "aplicacionBlog/buscarRubro.html")

@login_required
def buscarRubro2(request):
    if request.GET ['rubro']:
        rubro = request.GET['rubro']
        trabajos = Trabajo.objects.filter(rubro__icontains=rubro)
        return render(request, "aplicacionBlog/resultadosRubros.html", {"rubro": rubro, "trabajos": trabajos})
    return HttpResponse("No fueron ingresados datos")  

@login_required
def buscarNombre(request):
    return render(request, "aplicacionBlog/buscarNombre.html")

@login_required
def buscarNombre2(request):
    if request.GET ['nombre']:
        nombre = request.GET['nombre']
        trabajadores = Trabajador.objects.filter(nombre__icontains=nombre)
        return render(request, "aplicacionBlog/resultadosNombres.html", {"nombre": nombre, "trabajadores": trabajadores})
    return HttpResponse("No fueron ingresados datos")  

@login_required
def buscarHabilidades(request):
    return render(request, "aplicacionBlog/buscarHabilidades.html")

@login_required
def buscarHabilidades2(request):
    if request.GET ['habilidades']:
        habilidades = request.GET['habilidades']
        trabajadores = Trabajador.objects.filter(habilidades__icontains=habilidades)
        return render(request, "aplicacionBlog/resultadosHabilidades.html", {"habilidades": habilidades, "trabajadores": trabajadores})
    return HttpResponse("No fueron ingresados datos") 
  
@login_required
def buscarTrabajador(request):
    return render(request, "aplicacionBlog/buscarTrabajador.html")

@login_required
def buscarTrabajador2(request):
    if request.GET ['trabajador']:
        trabajador = request.GET['trabajador']
        recomendaciones = Recomendacion.objects.filter(trabajador__icontains=trabajador)
        return render(request, "aplicacionBlog/resultadosRecomendaciones.html", {"trabajador": trabajador, "recomendaciones": recomendaciones})
    return HttpResponse("No fueron ingresados datos")  






class RecomendacionList(LoginRequiredMixin, ListView):
    model = Recomendacion
class RecomendacionCreate(LoginRequiredMixin, CreateView):
    model = Recomendacion
    fields = ['trabajador', 'puntaje', 'comentarios']
    success_url = reverse_lazy('recomendaciones')
class RecomendacionDetail(LoginRequiredMixin, DetailView):
    model = Recomendacion
class RecomendacionUpdate(LoginRequiredMixin, UpdateView):
    model = Recomendacion
    fields = ['trabajador', 'puntaje', 'comentarios']
    success_url = reverse_lazy('recomendaciones')
class RecomendacionDelete(LoginRequiredMixin, DeleteView):
    model = Recomendacion
    success_url = reverse_lazy('recomendaciones')
    
        
class TrabajadorList(LoginRequiredMixin, ListView):
    model = Trabajador
class TrabajadorCreate(LoginRequiredMixin, CreateView):
    model = Trabajador
    fields = ['nombre', 'edad', 'telefono', 'rubro', 'habilidades']
    success_url = reverse_lazy('trabajador')
class TrabajadorDetail(LoginRequiredMixin, DetailView):
    model = Trabajador
class TrabajadorUpdate(LoginRequiredMixin, UpdateView):
    model = Trabajador
    fields = ['nombre', 'edad', 'telefono', 'rubro', 'habilidades']
    success_url = reverse_lazy('trabajador')
class TrabajadorDelete(LoginRequiredMixin, DeleteView):
    model = Trabajador
    success_url = reverse_lazy('trabajador')

    
    
class TrabajoList(LoginRequiredMixin, ListView):
    model = Trabajo  
class TrabajoCreate(LoginRequiredMixin, CreateView):
    model = Trabajo
    fields = ['titulo', 'descripcion', 'rubro', 'salario_ofrecido']
    success_url = reverse_lazy('trabajo')  
class TrabajoDetail(LoginRequiredMixin, DetailView):
    model = Trabajo 
class TrabajoUpdate(LoginRequiredMixin, UpdateView):
    model = Trabajo
    fields = ['titulo', 'descripcion', 'rubro', 'salario_ofrecido']
    success_url = reverse_lazy('trabajo')  
class TrabajoDelete(LoginRequiredMixin, DeleteView):
    model = Trabajo 
    success_url = reverse_lazy('trabajo') 
    
    
    
    
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                    
                return render(request, "aplicacionBlog/base.html", {"mensaje":f"Hola {usuario}"})
            else:
                return render(request, "aplicacionBlog/login.html", {"form":miForm, "mensaje": "Datos Invalidos"})
        else:
            return render(request, "aplicacionBlog/login.html", {"form":miForm, "mensaje": "Datos Invalidos"})
        
    miForm = AuthenticationForm()
    
    return render(request, "aplicacionBlog/login.html", {"form":miForm})


def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacionBlog/base.html", {"mensaje":"Usuario Creado"})
    else:
            form = RegistroUsuariosForm()
            
    return render(request, "aplicacionBlog/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2  = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacionBlog/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacionBlog/editarPerfil.html", {"form": form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacionBlog/editarPerfil.html", {'form': form, 'Usuario':usuario.username})


# ... your imports and other code ...

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # Store the avatar ID in the session
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacionBlog/base.html")

    else:
        form = AvatarFormulario()
        
    return render(request, "aplicacionBlog/agregarAvatar.html", {'form': form})

