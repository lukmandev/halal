from rest_framework.serializers import ModelSerializer
from .models import Time


class TimeSerializer(ModelSerializer):

    class Meta:
        model = Time
        fields = (
            'id',
            'date',
            'first_time',
            'second_time',
            'third_time',
            'fourth_time',
            'fifth_time',
            'sixth_time'
        )
