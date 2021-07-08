from django.shortcuts import render, reverse
from django.http import HttpResponse


def home_view(request):
    msg = 'Главная страница'
    return HttpResponse(msg)


def dish_view(request, dish_name):
    context = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
        'Ошибка': 'Нет данных'
    }
    servings = request.GET.get('servings')
    for key, value in context.items():
        if dish_name == key:
            final = '; ''<br/>'.join([f'{key_1.capitalize()}: {value_1}' for key_1, value_1 in value.items()])
            return HttpResponse(f'{dish_name}:<br/>{final}')
        if dish_name == key and servings is not None:
            result = '; ''<br/>'.join([f'{key_1.capitalize()}: {int(value_1) * int(servings)}'
                                       for key_1, value_1 in value.items()])
            return HttpResponse(f'{dish_name}:<br/>{result}')
    else:
        return HttpResponse('Такого рецепта нет в базе')
