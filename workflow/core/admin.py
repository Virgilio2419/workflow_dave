from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Capataz)
admin.site.register(Supervisor)
admin.site.register(Trabajador)
admin.site.register(Obra)
admin.site.register(Tarea)
admin.site.register(Pagos)