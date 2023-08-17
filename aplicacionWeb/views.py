from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    return render(request, "aplicacionWeb/base1.html")

def contacto(request):
    return render(request, "aplicacionWeb/contacto.html")

def sobremi(request):
    return render(request, "aplicacionWeb/sobremi.html")

def noticia1(request):
    return render(request, "aplicacionWeb/noticia1.html")

def noticia2(request):
    return render(request, "aplicacionWeb/noticia2.html")

def noticia3(request):
    return render(request, "aplicacionWeb/noticia3.html")

def noticia4(request):
    return render(request, "aplicacionWeb/noticia4.html")


#

def contacto_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return render(request, 'aplicacionWeb/contacto.html', {'success': True})

    return render(request, 'aplicacionWeb/contacto.html', {'success': False})
