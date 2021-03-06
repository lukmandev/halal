from rest_framework.serializers import ModelSerializer

from applications.models import Application


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = (
            'id',
            'company_name',
            'address',
            'product_type',
            'name',
            'phone'
        )
