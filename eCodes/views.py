from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ECode
from .serializers import ECodeSerializer


class ECodeMVS(ListAPIView, RetrieveAPIView):
    queryset = ECode.objects.all()
    serializer_class = ECodeSerializer
    lookup_field = 'id'