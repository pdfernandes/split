from rest_framework import serializers
from .models import Tab, Profile


class TabSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tab
        fields = ['id', 'title', 'owner', 'participants', 'created_at', 'updated_at']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user', 'created_at', 'updated_at']
