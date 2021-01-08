from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
        
class JugadoresForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['jug_nombre', 'fecha_nacimiento', 'dorsal', 'posicion', 'equipo', 'image']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['equipo_nombre', 'club', 'entrenador', 'categoria']
    
class PartidoForm(forms.ModelForm):
    
    class Meta:
        model = Partido
        fields = ['campo', 'fecha', 'n_jornada', 'equipo', 'rival', 'fecha', 'resultado_equipo', 'resultado_rival']
        widgets = {
            'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'}),
        }

class EstPartidoForm(forms.ModelForm):

    class Meta:
        model = DatosPartido
        fields = ['jugador_convocado', 'partido', 'titular', 'minutos_jugados', 'goles']
       
   