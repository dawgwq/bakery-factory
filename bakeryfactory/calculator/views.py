from django.shortcuts import render
from django.http import HttpResponse
from .models import Order


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    total_resources, measure = order.calculate_total_resources()
    return render(request, 'order_detail.html', {'order': order, 'total_resources': total_resources, 'measure':measure})