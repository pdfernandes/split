from rest_framework import serializers
from .models import Tab


class TabSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tab
        fields = ['id', 'title', 'owner', 'participants', 'created_at', 'updated_at']
