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
    for recipes in context:
        meal = recipes[0]
        content = recipes[1]
        if dish_name in meal:
            final = f'{meal}:\n' + '\n'.join(f'{con[0]}, {con[1]} {con[2]}' for con in content)
            return HttpResponse(final)
        else:
            return render(request, 'calculator/index.html', context)

