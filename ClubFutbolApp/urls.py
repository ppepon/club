from django.conf.urls import url
from django.urls import path
from ClubFutbolApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', Inicio.as_view(), name="index"),
    path('registro/', registro, name="registro"),
    #path('jugadores/', Jugadores.as_view(), name="jugadores"),
    path('jugadores/<int:pk>', Jugadores.as_view(), name="jugadores"),
    path('crear_jugador/', login_required(crearJugador.as_view()), name="crear_jugador"),
    path('est_jugadores/<int:pk>/', estJugador.as_view(), name="est_jugadores"),
    path('equipos/', Equipos.as_view(), name="equipos"),
    path('equipos/<str:pk>', Equiposfil.as_view(), name="Equiposfil"),
    path('crear_equipo/', login_required(crearEquipo.as_view()), name="crear_equipo"),
    path('crear_partido/', login_required(crearPartido.as_view()), name="crear_partido"),
    path('est_equipo/<int:pk>/', estPartido.as_view(), name="est_equipo"),
    path('partidos/<int:pk>/', listaPartidos.as_view(), name="partidos"),
    path('crear_est_partido/', crearEstPartido.as_view(), name="crear_est_partido"),
    path('editar_est_partido/<int:pk>', editarEstPartido.as_view(), name="editar_est_partido"),
    
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)