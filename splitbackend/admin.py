from django.contrib import admin
from splitbackend.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']


admin.site.register(Profile, ProfileAdmin)
