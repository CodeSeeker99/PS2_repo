from django.db import models

# Create your models here.
class PytorchModel(models.Model):
    name = models.CharField(max_length=40, blank=False, unique=True)
    desc = models.CharField(max_length=100, blank=False)
    last_updated = models.DateField(auto_now_add=True)