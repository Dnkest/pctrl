# Generated by Django 3.0 on 2019-12-15 00:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='control',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='control',
            name='maximum_rabi_rate',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='control',
            name='polar_angle',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='control',
            name='type',
            field=models.CharField(choices=[('PRIMITIVE', 'Primitive'), ('CORPSE', 'CORPSE'), ('GAUSSIAN', 'Gaussian'), ('CINBB', 'CinBB'), ('CINSK', 'CinSK')], max_length=60),
        ),
    ]
