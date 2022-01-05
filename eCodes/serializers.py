from rest_framework.serializers import ModelSerializer
from .models import ECode


class ECodeSerializer(ModelSerializer):

    class Meta:
        model = ECode
        fields = "__all__"
