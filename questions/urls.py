from django.urls import path
from .views import QuestionMVS

plural = {
    'get': 'list',
    'post': 'create',
}

single = {
    'get': 'retrieve',
}

urlpatterns = [
    path('all/', QuestionMVS.as_view(plural)),
    path('<int:id>/', QuestionMVS.as_view(single))
]