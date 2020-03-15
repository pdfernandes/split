from django.db import models
from .profile import Profile
from .item import Item
from django.core.validators import MinValueValidator, MinLengthValidator


class Split(models.Model):
    def __str__(self):
        return self.percent
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='participated_splits')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='splits')
    percent = models.DecimalField(max_digits=4, decimal_places=3, default=1, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
