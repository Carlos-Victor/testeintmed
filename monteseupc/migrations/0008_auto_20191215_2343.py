# Generated by Django 2.2.7 on 2019-12-16 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monteseupc', '0007_auto_20191215_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placa_mae',
            name='memom_suportada',
            field=models.IntegerField(choices=[('8', '8'), ('12', '12'), ('16', '16'), ('32', '32'), ('64', '64')], verbose_name='Memoria suportada'),
        ),
    ]
