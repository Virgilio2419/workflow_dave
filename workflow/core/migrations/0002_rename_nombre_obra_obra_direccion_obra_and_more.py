# Generated by Django 5.0.7 on 2024-07-17 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obra',
            old_name='Nombre_obra',
            new_name='direccion_obra',
        ),
        migrations.RenameField(
            model_name='obra',
            old_name='dirección_obra',
            new_name='nombre_obra',
        ),
        migrations.RenameField(
            model_name='obra',
            old_name='teléfono_obra',
            new_name='telefono_obra',
        ),
    ]
