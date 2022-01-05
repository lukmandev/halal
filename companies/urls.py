from django.urls import path

from companies.views import CategoriesMVS, CompanyMVS, ProductMVS, CompaniesMVS

plural = {
    'get': 'list'
}

single = {
    'get': 'retrieve',
    'delete': 'destroy'
}

urlpatterns = [
    path('category/all/', CategoriesMVS.as_view(plural)),
    path('category/<int:id>/', CategoriesMVS.as_view(single)),
    path('category/<int:category_id>/companies/', CompaniesMVS.as_view(plural)),

    path('company/all/', CompanyMVS.as_view(plural)),
    path('company/<int:id>/', CompanyMVS.as_view(single)),
    path('company/<int:company_id>/products/', ProductMVS.as_view(plural)),
]