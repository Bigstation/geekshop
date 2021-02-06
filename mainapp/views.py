from django.shortcuts import render

import datetime

from mainapp.models import Product, ProductCategory

# Create your views here.
# контроллер = функция
# MVC = Model View Controller
# MVT = Model View Template - в Джанго
# вьюха (view) = контроллер = функция

def index(request):
    return render(request, 'mainapp/index.html')

def products(request, id=None):
    context = {
        'data': datetime.date.today(),
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)