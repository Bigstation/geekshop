from basket.models import Basket

def busket_count(request):
    user = request.user
    if user.is_authenticated:
        counter = Basket.objects.filter(user=user).count()
    else:
        counter = 0

    return {'busket_count': counter}