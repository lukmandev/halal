from rest_framework.generics import ListAPIView, RetrieveAPIView
from banners.models import Banner
from banners.serializers import BannerSerializer


class BannerAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerRetrieveAPIView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = 'id'
