from django.shortcuts import render
import datetime

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
    }
    return render(request, 'mainapp/products.html', context)