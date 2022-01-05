from django.urls import path
from .views import BannerAPIView, BannerRetrieveAPIView

urlpatterns = [
    path('all/', BannerAPIView.as_view()),
    path('<int:id>/', BannerRetrieveAPIView.as_view())
]
