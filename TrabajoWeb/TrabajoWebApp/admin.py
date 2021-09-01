from django.contrib import admin
from formulario.models import Cargo, Formulario, Ofertas
from pregunta.models import PreguntaUnica , PreguntasBlog
from work.models import PreguntaMotivacional,Worksample
# Register your models here.

class OfertaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Cargo)
admin.site.register(Ofertas ,OfertaAdmin)
admin.site.register(Formulario)


admin.site.register(PreguntaUnica)

admin.site.register(PreguntasBlog)

admin.site.register(PreguntaMotivacional)

admin.site.register(Worksample)

