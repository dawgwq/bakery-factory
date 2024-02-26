
from django.urls import path

from . import views

urlpatterns = [
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/', views.order_list, name ='order_list'),
]