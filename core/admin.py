from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin (admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')  # o que quer que aparece dentro do django na parte de Core
    list_filter = ('titulo', 'data_evento',) # sempre tem que ter a vírgula no final, do contrário dá erro

admin.site.register(Evento, EventoAdmin)