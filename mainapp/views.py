from django.shortcuts import render

import datetime

from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# контроллер = функция
# MVC = Model View Controller
# MVT = Model View Template - в Джанго
# вьюха (view) = контроллер = функция

def index(request):
    return render(request, 'mainapp/index.html')


# def products(request, category_id=None):
#     context = {
#         'data': datetime.date.today(),
#         'categories': ProductCategory.objects.all(),
#         'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#     }
#
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('-price'), per_page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'data': datetime.date.today(),
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }

    return render(request, 'mainapp/products.html', context)
