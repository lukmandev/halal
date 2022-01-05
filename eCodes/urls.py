from django.urls import path
from .views import ECodeMVS


urlpatterns = [
    path('<int:id>/', ECodeMVS.as_view()),
    path('all/', ECodeMVS.as_view())
]