from django.db import models
from django.contrib.auth.models import User
# Create your models here.


RUBRO_CHOICES = [
    ('Tecnología', 'Tecnología'),
    ('Salud', 'Salud'),
    ('Educación', 'Educación'),
    ('Gastronomía', 'Gastronomía'),
    ('Construcción', 'Construcción'),
    ('Arte y Entretenimiento', 'Arte y Entretenimiento'),
    ('Ventas', 'Ventas'),
    ('Servicios', 'Servicios'),
    ('Pintura', 'Pintura'),
    ('Transporte', 'Transporte'),
    ('Plomeria', 'Plomeria'),
    ('Electricidad', 'Electricidad'),
]

class Trabajo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    rubro = models.CharField(max_length=50, choices=RUBRO_CHOICES)
    salario_ofrecido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    rubro = models.CharField(max_length=50, choices=RUBRO_CHOICES)
    habilidades = models.TextField()

    def __str__(self):
        return self.nombre

class Vinculacion(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trabajo.titulo} - {self.trabajador.nombre}"

class Recomendacion(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    puntaje = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Recomendación de {self.trabajador.nombre}"


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Trabajador)
def crear_vinculacion(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # Encuentra un trabajo con el mismo rubro que el trabajador
        trabajo_correspondiente = Trabajo.objects.filter(rubro=instance.rubro).first()

        if trabajo_correspondiente:
            Vinculacion.objects.create(trabajo=trabajo_correspondiente, trabajador=instance)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return f"{self.user} [{self.imagen}]"