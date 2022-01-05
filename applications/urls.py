from django.urls import path
from .views import ApplicationAPIView

urlpatterns = [
    path('', ApplicationAPIView.as_view())
]