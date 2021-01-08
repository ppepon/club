# Generated by Django 3.1.2 on 2020-12-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubFutbolApp', '0010_auto_20201223_0929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partido',
            options={'ordering': ['fecha', 'equipo'], 'verbose_name': 'partido', 'verbose_name_plural': 'partidos'},
        ),
        migrations.AlterField(
            model_name='partido',
            name='resultado_equipo',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='partido',
            name='resultado_rival',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]