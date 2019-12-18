# Generated by Django 2.2.7 on 2019-12-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monteseupc', '0010_auto_20191215_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='memoria',
            name='tamanho_da_memoria',
            field=models.CharField(choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB'), ('64GB', '64GB')], default=1, max_length=50, verbose_name='Tamanho da Memoria'),
            preserve_default=False,
        ),
    ]