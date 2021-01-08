from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from .forms import *


class Inicio(LoginRequiredMixin, TemplateView):
    template_name= 'ClubFutbolApp/Home.html'

class Jugadores(ListView):
    model= Jugador
    template_name='ClubFutbolApp/jugadores.html'
    context_object_name='jugadores'
    def get_queryset(self):
        qs=super(Jugadores, self).get_queryset()
        return qs.filter(equipo=self.request.resolver_match.kwargs['pk'])

class crearJugador(CreateView):
    model= Jugador
    template_name= 'ClubFutbolApp/crear_jugador.html'
    form_class= JugadoresForm
    success_url= '/equipos'

class estJugador(ListView):
    model= DatosPartido
    template_name='ClubFutbolApp/est_jugadores.html'
    context_object_name='datospartidos'
    
    def get_queryset(self):
        qs=super(estJugador, self).get_queryset()
        return qs.filter(jugador_convocado=self.request.resolver_match.kwargs['pk'])

class crearEquipo(CreateView):
    model= Equipo
    template_name= 'ClubFutbolApp/crear_equipo.html'
    form_class= EquipoForm
    success_url= '/equipos'

class Equipos(ListView):
    model= Equipo
    template_name='ClubFutbolApp/equipos.html'
    context_object_name='equipos'
    queryset= Equipo.objects.all()

class Equiposfil(ListView):
    model= Equipo
    template_name='ClubFutbolApp/equipos.html'
    context_object_name='equipos'
    #queryset= Equipo.objects.all()
    def get_queryset(self):
        qs=super(Equiposfil, self).get_queryset()
        return qs.filter(equipo_nombre__icontains=self.request.resolver_match.kwargs['pk'])

class crearPartido(CreateView):
    model= Partido
    template_name= 'ClubFutbolApp/crear_partido.html'
    form_class= PartidoForm
    success_url= '/equipos'

class listaPartidos(ListView):
    model= Partido
    template_name='ClubFutbolApp/partidos.html'
    context_object_name='partidos'
    #queryset= Partido.objects.all()
    
    def get_queryset(self):
        qs=super(listaPartidos, self).get_queryset()
        return qs.filter(equipo=self.request.resolver_match.kwargs['pk'])

class crearEstPartido(CreateView):
    model= DatosPartido
    template_name= 'ClubFutbolApp/crear_est_partido.html'
    form_class= EstPartidoForm
    success_url= '/equipos'

class editarEstPartido(UpdateView):
    model= DatosPartido
    template_name= 'ClubFutbolApp/crear_est_partido.html'
    form_class= EstPartidoForm
    success_url= '/equipos'


class estPartido(ListView):
    model= DatosPartido
    template_name='ClubFutbolApp/est_equipo.html'
    context_object_name='datospartidos'
    
    def get_queryset(self):
        qs=super(estPartido, self).get_queryset()
        return qs.filter(partido=self.request.resolver_match.kwargs['pk'])

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="/")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)

    