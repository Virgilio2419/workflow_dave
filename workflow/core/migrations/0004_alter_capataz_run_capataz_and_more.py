# Generated by Django 5.0.7 on 2024-07-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_nombre_tarea_tarea_nombre_tarea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capataz',
            name='Run_capataz',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='Run_supervisor',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='Run_trabajador',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]