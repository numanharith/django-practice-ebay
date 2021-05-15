from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', views_index, name='products_index'),
    path('show/<uuid:pk>', view_show, name='product_show'),
    path('category/', view_create_category, name='category_create'),
]