from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "user_order_history/<order_number>",
        views.user_order_history,
        name="user_order_history",
    ),
] 
