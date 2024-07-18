from django.db import models


# Create your models here.

class Capataz(models.Model):
    Run_capataz = models.CharField(max_length=20,unique=True)
    nombres_capataz = models.CharField(max_length=100)
    ap_pat_capataz = models.CharField(max_length=50)
    ap_mat_capataz = models.CharField(max_length=50)
    dirección_capataz = models.CharField(max_length=200)
    telefono_capataz = models.CharField(max_length=20, blank=True, null=True)
    telefono2_capataz = models.CharField(max_length=20, blank=True, null=True)
    celular_capataz = models.CharField(max_length=20)
    mail_capataz = models.EmailField()

    def __str__(self):
        return f'{self.nombres_capataz} {self.ap_pat_capataz} {self.ap_mat_capataz}'

class Supervisor(models.Model):
    Run_supervisor = models.CharField(max_length=20,unique=True)
    nombres_supervisor = models.CharField(max_length=100)
    ap_pat_supervisor = models.CharField(max_length=50)
    ap_mat_supervisor = models.CharField(max_length=50)
    dirección_supervisor = models.CharField(max_length=200)
    telefono_supervisor = models.CharField(max_length=20, blank=True, null=True)
    telefono2_supervisor = models.CharField(max_length=20, blank=True, null=True)
    celular_supervisor = models.CharField(max_length=20)
    mail_supervisor = models.EmailField()
    capataz = models.ForeignKey(Capataz, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombres_supervisor} {self.ap_pat_supervisor} {self.ap_mat_supervisor}'

class Trabajador(models.Model):
    Run_trabajador = models.CharField(max_length=20,unique=True)
    nombres_trabajador = models.CharField(max_length=100)
    ap_pat_trabajador = models.CharField(max_length=50)
    ap_mat_trabajador = models.CharField(max_length=50)
    dirección_trabajador = models.CharField(max_length=200)
    telefono_trabajador = models.CharField(max_length=20, blank=True, null=True)
    telefono2_trabajador = models.CharField(max_length=20, blank=True, null=True)
    celular_trabajador = models.CharField(max_length=20)
    mail_trabajador = models.EmailField()
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombres_trabajador} {self.ap_pat_trabajador} {self.ap_mat_trabajador}'

class Obra(models.Model):
    nombre_obra = models.CharField(max_length=200)
    direccion_obra = models.CharField(max_length=200)
    telefono_obra = models.CharField(max_length=20)
    mail_obra = models.EmailField()
    fecha_ini_obra = models.DateField()
    fecha_fin_obra = models.DateField(blank=True, null=True)
    supervisor_obra = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
    capataz_obra = models.ForeignKey(Capataz, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre_obra

class Tarea(models.Model):
    UNIDAD_MEDIA_CHOICES = [
        ('ml', 'Metros Lineales'),
        ('m2', 'Metros Cuadrados'),
    ]
    codigo_tarea = models.CharField(max_length=50, unique=True, blank=True, null=True, editable=False)
    nombre_tarea = models.CharField(max_length=200)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    id_obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    id_capataz = models.ForeignKey(Capataz, on_delete=models.CASCADE)
    unidad_media = models.CharField(max_length=2, choices=UNIDAD_MEDIA_CHOICES)
    cantidad = models.FloatField()
    valor = models.FloatField()
    fecha_ini = models.DateField()
    fecha_reasign = models.DateField(blank=True, null=True)
    fecha_finalizado = models.DateField(blank=True, null=True)
    unidades_efectivas = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.fecha_reasign and not self.fecha_finalizado:
            self.fecha_finalizado = self.fecha_reasign
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.nombre_tarea

class Pagos(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    monto = models.FloatField()
    fecha_pago = models.DateField()

    def __str__(self):
        return f'Pago a {self.trabajador} por {self.tarea}'
