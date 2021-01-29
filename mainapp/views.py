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
        'products': [
            {'img': '/static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'material': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             },
            {'img': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Синяя куртка The North Face',
             'price': '23 725,00 руб.',
             'material': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             },
            {'img': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00 руб.',
             'material': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             },
            {'img': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00 руб.',
             'material': 'Плотная ткань. Легкий материал.',
             },
            {'img': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.',
             'material': 'Гладкий кожаный верх. Натуральный материал.',
             },
            {'img': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00 руб.',
             'material': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             }
        ]
    }
    return render(request, 'mainapp/products.html', context)