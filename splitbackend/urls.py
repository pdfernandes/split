from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import user_create, Hello


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('hello/', Hello.as_view()),
    path('user/', user_create)
]
