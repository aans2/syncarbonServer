from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

class Bomba(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, blank=False)
    type = models.PositiveSmallIntegerField(
        default = 1,
        choices = [
        (0, 'Alcool'),
        (1, 'Diesel'),
    ])

    def __str__(self):
        return str(self.name)

class Combustivel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    bomba = models.ForeignKey(Bomba, on_delete=models.CASCADE)
    valor = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return str(self.valor)
