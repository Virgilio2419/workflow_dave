from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('capataces/', capataz_list, name='capataz_list'),
    path('capataces/create/', capataz_create, name='capataz_create'),
    path('capataces/update/<int:pk>/', capataz_update, name='capataz_update'),
    path('capataces/delete/<int:pk>/', capataz_delete, name='capataz_delete'),
# Capataz URLs
    path('capataces/', capataz_list, name='capataz_list'),
    path('capataces/create/', capataz_create, name='capataz_create'),
    path('capataces/update/<int:pk>/', capataz_update, name='capataz_update'),
    path('capataces/delete/<int:pk>/', capataz_delete, name='capataz_delete'),

    # Supervisor URLs
    path('supervisores/', supervisor_list, name='supervisor_list'),
    path('supervisores/create/', supervisor_create, name='supervisor_create'),
    path('supervisores/update/<int:pk>/', supervisor_update, name='supervisor_update'),
    path('supervisores/delete/<int:pk>/', supervisor_delete, name='supervisor_delete'),

    # Trabajador URLs
    path('trabajadores/', trabajador_list, name='trabajador_list'),
    path('trabajadores/create/', trabajador_create, name='trabajador_create'),
    path('trabajadores/update/<int:pk>/', trabajador_update, name='trabajador_update'),
    path('trabajadores/delete/<int:pk>/', trabajador_delete, name='trabajador_delete'),

    # Obra URLs
    path('obras/', obra_list, name='obra_list'),
    path('obras/create/', obra_create, name='obra_create'),
    path('obras/update/<int:pk>/', obra_update, name='obra_update'),
    path('obras/delete/<int:pk>/', obra_delete, name='obra_delete'),

    # Tarea URLs
    path('tareas/', tarea_list, name='tarea_list'),
    path('tareas/create/', tarea_create, name='tarea_create'),
    path('tareas/update/<int:pk>/', tarea_update, name='tarea_update'),
    path('tareas/delete/<int:pk>/', tarea_delete, name='tarea_delete'),
    path('tareas/reasignar/<int:tarea_id>/', reasignar_tarea, name='tarea_reasignar'),
    path('tareas/terminar/<int:tarea_id>/', tarea_terminar, name='tarea_terminar'),  # Definición de la URL para terminar tarea
    # Otras URLs de tu aplicación...

    # Pagos URLs
    path('pagos/', pagos_list, name='pagos_list'),
    path('pagos/create/', pagos_create, name='pagos_create'),
    path('pagos/update/<int:pk>/', pagos_update, name='pagos_update'),
    path('pagos/delete/<int:pk>/', pagos_delete, name='pagos_delete'),
]