# Generated by Django 3.1.2 on 2020-12-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubFutbolApp', '0004_auto_20201204_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospartido',
            name='titular',
            field=models.BooleanField(blank=True, choices=[('Titular', 'Titular'), ('Suplente', 'Suplente')], null=True),
        ),
    ]
