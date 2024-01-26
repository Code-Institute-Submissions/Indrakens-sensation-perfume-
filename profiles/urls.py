from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"), 
    path(
        "update_profile/<profile>", 
        views.update_profile, 
        name="update_profile"), 
    path(
        "user_order_history/<order_number>",
        views.user_order_history,
        name="user_order_history",
    ),
    path(
        "delete/<order_number>/",
        views.delete_order_history,
        name="delete_order_history",
    ),
] 
