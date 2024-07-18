from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')


def login_view(request):
    return render(request, 'core/login.html')


# Capataz Views
def capataz_list(request):
    capataces = Capataz.objects.all()
    return render(request, 'core/capataz_list.html', {'capataces': capataces})

def capataz_create(request):
    if request.method == 'POST':
        form = CapatazForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capataz_list')
    else:
        form = CapatazForm()
    return render(request, 'core/capataz_form.html', {'form': form})

def capataz_update(request, pk):
    capataz = get_object_or_404(Capataz, pk=pk)
    if request.method == 'POST':
        form = CapatazForm(request.POST, instance=capataz)
        if form.is_valid():
            form.save()
            return redirect('capataz_list')
    else:
        form = CapatazForm(instance=capataz)
    return render(request, 'core/capataz_form.html', {'form': form})

def capataz_delete(request, pk):
    capataz = get_object_or_404(Capataz, pk=pk)
    if request.method == 'POST':
        capataz.delete()
        return redirect('capataz_list')
    return render(request, 'core/capataz_confirm_delete.html', {'object': capataz})


# Supervisor Views
def supervisor_list(request):
    supervisores = Supervisor.objects.all()
    return render(request, 'core/supervisor_list.html', {'supervisores': supervisores})

def supervisor_create(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supervisor_list')
    else:
        form = SupervisorForm()
    return render(request, 'core/supervisor_form.html', {'form': form})

def supervisor_update(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            return redirect('supervisor_list')
    else:
        form = SupervisorForm(instance=supervisor)
    return render(request, 'core/supervisor_form.html', {'form': form})

def supervisor_delete(request, pk):
    supervisor = get_object_or_404(Supervisor, pk=pk)
    if request.method == 'POST':
        supervisor.delete()
        return redirect('supervisor_list')
    return render(request, 'core/supervisor_confirm_delete.html', {'object': supervisor})

# Trabajador Views
def trabajador_list(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'core/trabajador_list.html', {'trabajadores': trabajadores})

def trabajador_create(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm()
    return render(request, 'core/trabajador_form.html', {'form': form})

def trabajador_update(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'core/trabajador_form.html', {'form': form})

def trabajador_delete(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajador_list')
    return render(request, 'core/trabajador_confirm_delete.html', {'object': trabajador})

# Obra Views
def obra_list(request):
    obras = Obra.objects.all()
    return render(request, 'core/obra_list.html', {'obras': obras})

def obra_create(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obra_list')
    else:
        form = ObraForm()
    return render(request, 'core/obra_form.html', {'form': form})

def obra_update(request, pk):
    obra = get_object_or_404(Obra, pk=pk)
    if request.method == 'POST':
        form = ObraForm(request.POST, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('obra_list')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'core/obra_form.html', {'form': form})

def obra_delete(request, pk):
    obra = get_object_or_404(Obra, pk=pk)
    if request.method == 'POST':
        obra.delete()
        return redirect('obra_list')
    return render(request, 'core/obra_confirm_delete.html', {'object': obra})

# Tarea Views
def tarea_list(request):
    tareas = Tarea.objects.all()

    # Actualizar el campo codigo_tarea con la concatenación de ids
    for tarea in tareas:
        if tarea.trabajador_id:
            tarea.codigo_tarea = f"{tarea.id}-{tarea.trabajador_id}"

    return render(request, 'core/tarea_list.html', {'tareas': tareas})

def tarea_create(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm()
    return render(request, 'core/tarea_form.html', {'form': form})

def tarea_update(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea_list')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'core/tarea_form.html', {'form': form})

def tarea_delete(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tarea_list')
    return render(request, 'core/tarea_confirm_delete.html', {'object': tarea})


def reasignar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = ReasignarTareaForm(request.POST, tarea=tarea)
        if form.is_valid():
            nuevo_trabajador = form.cleaned_data['nuevo_trabajador']
            cantidad_reasignada = form.cleaned_data['cantidad_reasignada']

            # Actualizar la tarea original
            tarea.fecha_reasign = timezone.now()
            tarea.unidades_efectivas = tarea.cantidad - cantidad_reasignada
            tarea.cantidad -= cantidad_reasignada
            tarea.save()

            # Crear una nueva tarea para el nuevo trabajador
            nueva_tarea = Tarea.objects.create(
                nombre_tarea=tarea.nombre_tarea,
                trabajador=nuevo_trabajador,
                id_obra=tarea.id_obra,
                id_capataz=tarea.id_capataz,
                unidad_media=tarea.unidad_media,
                cantidad=cantidad_reasignada,
                valor=tarea.valor,
                fecha_ini=timezone.now()
            )

            messages.success(request, 'La tarea ha sido reasignada exitosamente.')
            return redirect('tarea_list')
    else:
        form = ReasignarTareaForm(tarea=tarea)

    return render(request, 'core/reasignar_tarea.html', {'form': form, 'tarea': tarea})

@require_POST
def tarea_terminar(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)

    if tarea.fecha_finalizado:
        messages.error(request, 'Esta tarea ya ha sido terminada anteriormente.')
    else:
        # Procesar la terminación de la tarea
        tarea.unidades_efectivas = tarea.cantidad  # Ejemplo, actualizar las unidades efectivas
        tarea.fecha_finalizado = timezone.now()   # Ejemplo, establecer la fecha de finalización

        tarea.save()

        messages.success(request, 'La tarea ha sido terminada exitosamente.')

    return redirect('tarea_list')

# Pagos Views
def pagos_list(request):
    pagos = Pagos.objects.all()
    return render(request, 'core/pagos_list.html', {'pagos': pagos})

def pagos_create(request):
    if request.method == 'POST':
        form = PagosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagos_list')
    else:
        form = PagosForm()
    return render(request, 'core/pagos_form.html', {'form': form})

def pagos_update(request, pk):
    pagos = get_object_or_404(Pagos, pk=pk)
    if request.method == 'POST':
        form = PagosForm(request.POST, instance=pagos)
        if form.is_valid():
            form.save()
            return redirect('pagos_list')
    else:
        form = PagosForm(instance=pagos)
    return render(request, 'core/pagos_form.html', {'form': form})

def pagos_delete(request, pk):
    pagos = get_object_or_404(Pagos, pk=pk)
    if request.method == 'POST':
        pagos.delete()
        return redirect('pagos_list')
    return render(request, 'core/pagos_confirm_delete.html', {'object': pagos})
