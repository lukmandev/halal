from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Category, Company, Product

# Serializers
from .serializers import CategorySerializer, CompanySerializer, CompanyRetrieveSerializer, ProductSerializer


# M_V_S
class CategoriesMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class CompanyMVS(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        company = Company.objects.filter(id=kwargs['id']).first()
        serializer = CompanyRetrieveSerializer(company, many=False).data

        return Response(data=serializer)


class ProductMVS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        company_products = Product.objects.filter(company_id=kwargs['company_id'])
        serializer = self.serializer_class(company_products, many=True).data

        return Response(data=serializer)


class CompaniesMVS(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        companies = Company.objects.filter(category_id=kwargs['category_id'])
        serializer = self.serializer_class(companies, many=True).data

        return Response(data=serializer)