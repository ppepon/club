from django.db import models

# Create your models here.

class Club(models.Model):
    club_nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to='ClubFutbolApp', null=True, blank=True)

    class Meta:
        verbose_name ='club'
        verbose_name_plural ='clubs'

    def __str__(self):
        return self.club_nombre

class Categoria(models.Model):
    cat_nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name ='categoria'
        verbose_name_plural ='categorias'

    def __str__(self):
        return self.cat_nombre

class Equipo(models.Model):
    equipo_nombre = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete = models.CASCADE)
    entrenador = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    class Meta:
        verbose_name ='equipo'
        verbose_name_plural ='equipos'

    def __str__(self):
        return self.equipo_nombre



class Posicion(models.Model):
    pos_nombre = models.CharField(max_length=20)

    class Meta:
        verbose_name ='posicion'
        verbose_name_plural ='posiciones'

    def __str__(self):
        return self.pos_nombre

class Jugador(models.Model):
    jug_nombre = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Jugadores', null=True, blank=True)
    fecha_nacimiento = models.DateField()
    dorsal = models.IntegerField()
    posicion = models.ForeignKey(Posicion, on_delete = models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete = models.CASCADE)

    class Meta:
        ordering = ["equipo", "jug_nombre"]
        verbose_name ='jugador'
        verbose_name_plural ='jugadores'

    def __str__(self):
        return "%s-%s" %(self.equipo,self.jug_nombre)

class Partido(models.Model):
    OPCIONES_DE_LUGAR = ('Casa', 'Casa'), ('Fuera', 'Fuera')
    fecha = models.DateTimeField()
    n_jornada = models.IntegerField(max_length=2)
    equipo = models.ForeignKey(Equipo, on_delete = models.CASCADE)
    rival = models.CharField(max_length=30)
    campo = models.CharField(max_length=5, choices = OPCIONES_DE_LUGAR, blank=True, null=True)
    resultado_equipo = models.PositiveSmallIntegerField(default=0)
    resultado_rival = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["fecha", "equipo"]
        verbose_name ='partido'
        verbose_name_plural ='partidos'

    def __str__(self):
        return "%s-%s" %(self.equipo,self.rival)
   

class DatosPartido(models.Model):
    #OPCIONES_DE_TITULAR = ('True', 'Titular'), ('False', 'Suplente')
    partido = models.ForeignKey(Partido, on_delete = models.CASCADE)
    jugador_convocado = models.ForeignKey(Jugador, on_delete = models.CASCADE)
    titular = models.BooleanField(blank=True, null=True)
    minutos_jugados = models.IntegerField()
    goles = models.IntegerField(default=0)

    class Meta:
        ordering = ["jugador_convocado"]
        verbose_name ='datospartido'
        verbose_name_plural ='datospartidos'
        








