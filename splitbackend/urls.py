from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import user_create, Hello, ParticipatedTabList, TabDetail, OwnedTabList


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('hello/', Hello.as_view()),
    path('user/', user_create),
    path('profile/tabs/', ParticipatedTabList.as_view()),
    path('profile/tab/<int:pk>/', TabDetail.as_view()),
    path('profile/owned_tabs/', OwnedTabList.as_view()),
]
