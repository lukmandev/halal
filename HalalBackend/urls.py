from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/codes/', include('eCodes.urls')),
    path('api/v1/companies/', include('companies.urls')),
    path('api/v1/times/', include('times.urls')),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/questions/', include('questions.urls')),
    path('api/v1/banners/', include('banners.urls')),
    path('api/v1/application/', include('applications.urls'))
] + doc_urls
