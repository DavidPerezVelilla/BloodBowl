# Generated by Django 3.2.8 on 2021-11-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='habilidades',
            field=models.CharField(max_length=200, verbose_name='Habilidades'),
        ),
    ]