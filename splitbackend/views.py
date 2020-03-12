import json
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Tab, Profile
from .serializers import TabSerializer, ProfileSerializer


class Hello(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World! If you are seeing this, you must be authenticated!'}
        return Response(content)


@api_view(['POST'])
def user_create(request):
    user_credentials = json.loads(request.body)
    try:
        user = User(username=user_credentials['username'], email=user_credentials['email'])
        user.set_password(user_credentials['password'])
        user.save()
        Profile.objects.create(user=user)
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'message': 'fail'}, status=status.HTTP_400_BAD_REQUEST)


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


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
