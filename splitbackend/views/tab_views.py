import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from splitbackend.models import Tab
from splitbackend.serializers import TabSerializer


class ParticipatedTabList(generics.ListAPIView):
    serializer_class = TabSerializer

    def get_queryset(self):
        return self.request.user.profile.tabs


class OwnedTabList(generics.ListAPIView):
    serializer_class = TabSerializer

    def get_queryset(self):
        return self.request.user.owned_tabs


class CreateTab(generics.CreateAPIView):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)


class TabDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TabSerializer

    def get_queryset(self):
        profile = self.request.user
        return Tab.objects.filter(profile=profile)
