# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0005_auto_20170616_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentes',
            name='IMC',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='estatura',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='peso',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='tipo_aborto',
            field=models.CharField(blank=True, choices=[('PRO', 'Provocados'), ('PER', 'Perdida')], max_length=10, null=True, verbose_name=' '),
        ),
    ]