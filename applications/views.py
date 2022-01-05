from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from applications.models import Application
from applications.serializers import ApplicationSerializer


class ApplicationAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
