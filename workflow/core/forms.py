from django import forms
from .models import *

class CapatazForm(forms.ModelForm):
    class Meta:
        model = Capataz
        fields = '__all__'

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'


class ReasignarTareaForm(forms.Form):
    nuevo_trabajador = forms.ModelChoiceField(queryset=Trabajador.objects.all(), label="Nuevo Trabajador")
    cantidad_reasignada = forms.FloatField(min_value=1, label="Cantidad a Reasignar")

    def __init__(self, *args, **kwargs):
        self.tarea = kwargs.pop('tarea')
        super().__init__(*args, **kwargs)

    def clean_cantidad_reasignada(self):
        cantidad_reasignada = self.cleaned_data.get('cantidad_reasignada')
        if self.tarea.unidades_efectivas is not None and self.tarea.unidades_efectivas > 0:
            raise forms.ValidationError("La tarea parece estar finalizada, valida esta informacion.")
        else:
            if cantidad_reasignada > self.tarea.cantidad:
                raise forms.ValidationError("La cantidad a reasignar no puede ser mayor a la cantidad de la tarea.")
        return cantidad_reasignada