from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import user_create, Hello, TabList, TabDetail, ProfileList


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('hello/', Hello.as_view()),
    path('user/', user_create),
    path('tabs/', TabList.as_view()),
    path('tabs/<int:pk>/', TabDetail.as_view()),
    path('profiles/', ProfileList.as_view())
]
