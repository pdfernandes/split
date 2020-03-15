from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    def __str__(self):
        return str(self.user.username)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
