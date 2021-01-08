from django.contrib import admin
from .models import Club, Equipo, Jugador, Categoria, Posicion, Partido, DatosPartido
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ClubAdmin(admin.ModelAdmin):
    list_display = ("club_nombre", "direccion", "ciudad", "email", "telefono", "imagen")

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("equipo_nombre", "entrenador")
    resources_class = EquipoResource

class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador
class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("jug_nombre", "dorsal", "equipo", "posicion", "image", "fecha_nacimiento")
    def get_queryset(self, request):
        return super(JugadorAdmin, self).get_queryset(request).order_by('equipo', 'jug_nombre')
    resources_class = JugadorResource

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("cat_nombre",)
    resources_class = CategoriaResource

class PosicionResource(resources.ModelResource):
    class Meta:
        model = Posicion
class PosicionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("pos_nombre",)
    resources_class = PosicionResource

class PartidoResource(resources.ModelResource):
    class Meta:
        model = Partido
class PartidoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("fecha", "n_jornada", "equipo", "resultado_equipo", "rival", "resultado_rival", "campo")
    fields = ["fecha", "n_jornada", ("equipo", "resultado_equipo"), ("rival", "resultado_rival"), "campo"]
    resources_class = PartidoResource

class DatosPartidoResource(resources.ModelResource):
    class Meta:
        model = DatosPartido
class DatosPartidoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("partido", "jugador_convocado", "titular", "minutos_jugados")
    resources_class = DatosPartido

admin.site.register(Club, ClubAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Posicion, PosicionAdmin)
admin.site.register(Partido, PartidoAdmin)
admin.site.register(DatosPartido, DatosPartidoAdmin)

