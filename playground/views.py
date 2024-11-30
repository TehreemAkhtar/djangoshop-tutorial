from django.db.models import Count, Sum, Min, Max, Avg, F
from django.shortcuts import render
from django.http import HttpResponse, request
from store.models import Product, Customer, Collection, Order, OrderItem, Cart, CartItem


def say_hello(request):


    return render(request, 'hello.html')