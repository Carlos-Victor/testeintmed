# Generated by Django 2.2.7 on 2019-12-10 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monteseupc', '0002_auto_20191209_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monte_seu_pc',
            name='placa_de_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monteseupc.Placa_de_video', verbose_name='Placa de Video'),
        ),
    ]