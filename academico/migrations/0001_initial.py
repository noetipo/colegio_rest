# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grado', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Grados',
                'verbose_name': 'Grado',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('materia', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Seccions',
                'verbose_name': 'Seccion',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Seccions',
                'verbose_name': 'Seccion',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('periodo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Periodos',
                'verbose_name': 'Periodo',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('tipo_persona', models.CharField(choices=[('1', 'Profesor'), ('2', 'Estudiante'), ('3', 'Director')], default=2, max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Personas',
                'verbose_name': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seccion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Grado')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Periodo')),
            ],
            options={
                'verbose_name_plural': 'Seccions',
                'verbose_name': 'Seccion',
            },
        ),
        migrations.AddField(
            model_name='matricula',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Persona'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academico.Seccion'),
        ),
        migrations.AddField(
            model_name='grado',
            name='materia',
            field=models.ManyToManyField(to='academico.Materia'),
        ),
    ]
