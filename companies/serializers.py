from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Company, Product


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title_ky', 'title_ru')


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'logo', 'category')


class CompanyRetrieveSerializer(ModelSerializer):

    category = SerializerMethodField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'logo', 'category')

    def get_category(self, obj):
        return CategorySerializer(Category.objects.filter(id=obj.id).first()).data


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title_ky', 'title_ru', 'photo', 'company')


class ProductRetrieveSerializer(ModelSerializer):

    company = SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title_ky', 'title_ru', 'photo', 'company')

    def get_company(self, obj):
        return CompanySerializer(Company.objects.get(id=obj.id)).data
