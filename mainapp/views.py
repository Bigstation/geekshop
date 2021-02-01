from django.shortcuts import render

import datetime

from mainapp.models import ProductCategory, Product

# Create your views here.
# контроллер = функция
# MVC = Model View Controller
# MVT = Model View Template - в Джанго
# вьюха (view) = контроллер = функция

def index(request):
    """Разная логика"""
    """Всяко разно"""
    return render(request, 'mainapp/index.html')

def products(request):
    context = {
        'data': datetime.date.today(),
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),



        #     {'img': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
        #      'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        #      'price': '2 890,00 руб.',
        #      'material': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
        #      }
        # ],

        # 'categories': ['Новинки', 'Одежда', 'Обувь', 'Аксесуары', 'Подарки']
    }
    return render(request, 'mainapp/products.html', context)