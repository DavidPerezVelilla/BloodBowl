# Generated by Django 3.2.8 on 2021-11-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_alter_jugador_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='desc',
            field=models.CharField(max_length=5000, null=True, verbose_name='Descripcion'),
        ),
    ]
