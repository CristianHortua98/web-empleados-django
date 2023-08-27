from django.contrib import admin
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'first_name', 'last_name', 'job', 'departamento', 'full_name')

    #Funcion para columna full_name
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name
    

    search_fields = ('first_name', 'last_name', 'job')
    list_filter = ('job', 'departamento', 'habilidades')
    filter_horizontal = ('habilidades',)


# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)