# Generated by Django 5.0.7 on 2024-07-17 14:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_capataz_run_capataz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='codigo_tarea',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]