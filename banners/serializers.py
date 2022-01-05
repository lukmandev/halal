from rest_framework.serializers import ModelSerializer

from banners.models import Banner


class BannerSerializer(ModelSerializer):

    class Meta:
        model = Banner
        fields = ('id', 'banner', 'creation_date', 'update_date')
