from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from .tab import Tab


class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    cost = models.DecimalField(max_digits=17, decimal_places=2, validators=[MinValueValidator(0)])
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
