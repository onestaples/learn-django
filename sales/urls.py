from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.listorder),
    path('customers/', views.listcustoms),
]
