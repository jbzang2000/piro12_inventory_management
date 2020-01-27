from django.urls import path
from .views import *

app_name = 'inventorymanage'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('item/create/', item_create, name='item_create'),
    path('item/<int:pk>/edit/', item_edit, name='item_edit'),
    path('item/<int:pk>/delete/', item_delete, name='item_delete'),
    path('item/<int:pk>/add/', item_amount_add, name='item_amount_add'),
    path('item/<int:pk>/sub/', item_amount_sub, name='item_amount_sub'),
    path('shop/', shop_list, name='shop_list'),
    path('shop/<int:pk>/', shop_detail, name='shop_detail'),
    path('shop/create/', shop_create, name='shop_create'),
    path('shop/<int:pk>/edit/', shop_edit, name='shop_edit'),
    path('shop/<int:pk>/delete/', shop_delete, name='shop_delete'),
]