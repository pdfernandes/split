import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from django.contrib.auth.models import User


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
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
    except Exception:
        return Response({'message': 'fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
