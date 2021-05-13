from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', views_index, name='products_index'),
    path('show/<uuid:pk>', views_show, name='product_show'),
]