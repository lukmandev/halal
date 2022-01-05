from rest_framework.viewsets import ModelViewSet

from .models import Time
from .serializers import TimeSerializer


class TimeMVS(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    lookup_field = 'date'
