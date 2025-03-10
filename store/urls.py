from django.urls import path
from .views import home, product_detail, search

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
]