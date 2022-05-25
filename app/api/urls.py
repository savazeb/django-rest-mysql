from django.urls import path
from .views import *

urlpatterns = [
    path('', apiOverview.as_view(), name='apiOverview'),
    path('product/list/', ShowAll.as_view(), name='list'),
    path('product/detail/<int:pk>/', ViewProduct.as_view(), name='detail'),
    path('product/create/', CreateProduct.as_view(), name='create'),
    path('product/update/<int:pk>/', UpdateProduct.as_view(), name='update'),
    path('product/delete/<int:pk>/', DeleteProduct.as_view(), name='delete'),
]
