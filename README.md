# GeekShop

    Проект интернет-магазина

#Выгрузка данных:

    python manage.py dumpdata mainapp.ProductCategory > categories.json

    python manage.py dumpdata mainapp.Product > products.json


#Загрузка данных:

    python manage.py loaddata mainapp/fixtures/categories.json

    python manage.py loaddata mainapp/fixtures/products.json


#SuperUser: 
    admin
#password: 
    admin

#Посмотреть версию Django:
    python -m django --version

#Установка зависимостей: 
    pip install -r requirements.txt

#Просмотр пакетов вирт окр:
    pip list

