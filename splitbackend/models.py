from django.db import models
from django.core.exceptions import ValidationError


class Profile(models.Model):
    def __str__(self):
        return str(self.id)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tab(models.Model):
    def __str__(self):
        return self.title
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owned_tabs')
    title = models.CharField(max_length=30, default='Outing')
    participants = models.ManyToManyField(Profile, related_name='tabs')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=17, decimal_places=2)
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.cost < 0:
            raise ValidationError("Cost must be atleast 0.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Item, self).save(*args, **kwargs)


class Split(models.Model):
    def __str__(self):
        return self.percent
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='participated_splits')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='splits')
    percent = models.DecimalField(max_digits=4, decimal_places=3, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
