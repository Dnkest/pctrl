from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Control(models.Model):
    CONTROL_TYPES = [
        ('PRIMITIVE', 'Primitive'),
        ('CORPSE', 'CORPSE'),
        ('GAUSSIAN', 'Gaussian'),
        ('CINBB', 'CinBB'),
        ('CINSK', 'CinSK')
    ]
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    type = models.CharField(blank=False, choices=CONTROL_TYPES, max_length=60)
    maximum_rabi_rate = models.FloatField(
                    validators=[MinValueValidator(0), MaxValueValidator(100)],
                    default=0
                )
    polar_angle = models.FloatField(
                    validators=[MinValueValidator(0), MaxValueValidator(1)],
                    default=0
                )
