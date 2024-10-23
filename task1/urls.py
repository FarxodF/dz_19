from django.urls import path
from .views import index, shop, cart, sign_up_by_django, Menu

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('menu/', Menu.as_view(), name='menu'),
    path('sign_up/', sign_up_by_django, name='sign_up'),
]