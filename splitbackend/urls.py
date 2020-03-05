from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import HelloView


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('hello/', HelloView.as_view())
]
