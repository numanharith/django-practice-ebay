from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('product/<uuid:product>', views_create, name='comment_create'),
]