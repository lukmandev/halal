from django.urls import path
from .views import TimeMVS

plural = {
    'get': 'list'
}

single = {
    'get': 'retrieve',
    'delete': 'destroy'
}

urlpatterns = [
    path('time/all/', TimeMVS.as_view(plural)),
    path('time/<slug:date>/', TimeMVS.as_view(single))
]