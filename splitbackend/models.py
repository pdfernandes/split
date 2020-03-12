from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    def __str__(self):
        return str(self.user.username)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tab(models.Model):
    def __str__(self):
        return self.title
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owned_tabs')
    title = models.CharField(max_length=30, default='Outing', validators=[MinLengthValidator(3)])
    participants = models.ManyToManyField(Profile, related_name='tabs', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    cost = models.DecimalField(max_digits=17, decimal_places=2, validators=[MinValueValidator(0)])
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Split(models.Model):
    def __str__(self):
        return self.percent
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='participated_splits')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='splits')
    percent = models.DecimalField(max_digits=4, decimal_places=3, default=1, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
