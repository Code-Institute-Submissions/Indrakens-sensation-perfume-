from django.urls import path
from . import views
from .webhooks import webhook 


urlpatterns = [
    path("", views.order_checkout, name="order_checkout"),
    path("order_checkout_success/<order_number>",
        views.order_checkout_success,
        name="order_checkout_success",),
    path('cache_checkout_data/',
         views.cache_checkout_data,
         name='cache_checkout_data'),     
    path("wh/", webhook, name="webhook"),
] 
