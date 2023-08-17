from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        


    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Nombre", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido", max_length=50, required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
        
        
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)
