from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationUserAPIView, ProfileAPIView, FavoriteAPIView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegistrationUserAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
    path('favorite/', FavoriteAPIView.as_view())
]
