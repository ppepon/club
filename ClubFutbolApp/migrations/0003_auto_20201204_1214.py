# Generated by Django 3.1.2 on 2020-12-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ClubFutbolApp', '0002_auto_20201204_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='dorsal',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('n_jornada', models.IntegerField()),
                ('rival', models.CharField(max_length=30)),
                ('campo', models.CharField(blank=True, choices=[('Casa', 'Casa'), ('Fuera', 'Fuera')], max_length=5, null=True)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubFutbolApp.equipo')),
            ],
            options={
                'verbose_name': 'partido',
                'verbose_name_plural': 'partidos',
            },
        ),
        migrations.CreateModel(
            name='DatosPartido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.BooleanField(choices=[('True', 'Titular'), ('False', 'Suplente')])),
                ('minutos_jugados', models.IntegerField()),
                ('goles', models.IntegerField()),
                ('jugador_convocado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubFutbolApp.jugador')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClubFutbolApp.partido')),
            ],
            options={
                'verbose_name': 'datospartido',
                'verbose_name_plural': 'datospartidos',
            },
        ),
    ]