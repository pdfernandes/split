from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from .profile import Profile


class Tab(models.Model):
    def __str__(self):
        return self.title
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owned_tabs')
    title = models.CharField(max_length=30, default='Outing', validators=[MinLengthValidator(3)])
    participants = models.ManyToManyField(Profile, related_name='tabs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
