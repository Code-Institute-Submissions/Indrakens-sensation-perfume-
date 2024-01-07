from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_checkout, name='order_checkout'),
    path('order_checkout_success/<order_number>', views.order_checkout_success, name='order_checkout_success'),
] 