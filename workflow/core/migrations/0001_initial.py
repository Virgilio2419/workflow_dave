# Generated by Django 5.0.7 on 2024-07-17 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capataz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Run_capataz', models.CharField(max_length=20)),
                ('nombres_capataz', models.CharField(max_length=100)),
                ('ap_pat_capataz', models.CharField(max_length=50)),
                ('ap_mat_capataz', models.CharField(max_length=50)),
                ('dirección_capataz', models.CharField(max_length=200)),
                ('telefono_capataz', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono2_capataz', models.CharField(blank=True, max_length=20, null=True)),
                ('celular_capataz', models.CharField(max_length=20)),
                ('mail_capataz', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Run_supervisor', models.CharField(max_length=20)),
                ('nombres_supervisor', models.CharField(max_length=100)),
                ('ap_pat_supervisor', models.CharField(max_length=50)),
                ('ap_mat_supervisor', models.CharField(max_length=50)),
                ('dirección_supervisor', models.CharField(max_length=200)),
                ('telefono_supervisor', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono2_supervisor', models.CharField(blank=True, max_length=20, null=True)),
                ('celular_supervisor', models.CharField(max_length=20)),
                ('mail_supervisor', models.EmailField(max_length=254)),
                ('capataz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.capataz')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_obra', models.CharField(max_length=200)),
                ('dirección_obra', models.CharField(max_length=200)),
                ('teléfono_obra', models.CharField(max_length=20)),
                ('mail_obra', models.EmailField(max_length=254)),
                ('fecha_ini_obra', models.DateField()),
                ('fecha_fin_obra', models.DateField(blank=True, null=True)),
                ('capataz_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.capataz')),
                ('supervisor_obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Run_trabajador', models.CharField(max_length=20)),
                ('nombres_trabajador', models.CharField(max_length=100)),
                ('ap_pat_trabajador', models.CharField(max_length=50)),
                ('ap_mat_trabajador', models.CharField(max_length=50)),
                ('dirección_trabajador', models.CharField(max_length=200)),
                ('telefono_trabajador', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono2_trabajador', models.CharField(blank=True, max_length=20, null=True)),
                ('celular_trabajador', models.CharField(max_length=20)),
                ('mail_trabajador', models.EmailField(max_length=254)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_tarea', models.CharField(max_length=200)),
                ('unidad_media', models.CharField(choices=[('ml', 'Mililitros'), ('m2', 'Metros Cuadrados')], max_length=2)),
                ('cantidad', models.FloatField()),
                ('valor', models.FloatField()),
                ('fecha_ini', models.DateField()),
                ('fecha_reasign', models.DateField(blank=True, null=True)),
                ('fecha_finalizado', models.DateField(blank=True, null=True)),
                ('unidades_efectivas', models.FloatField(blank=True, null=True)),
                ('id_capataz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.capataz')),
                ('id_obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.obra')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('fecha_pago', models.DateField()),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tarea')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trabajador')),
            ],
        ),
    ]