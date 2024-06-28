from django.shortcuts import render

DATA = {
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
    # можете добавить свои рецепты ;)
}

def recipe(request,dish:str):
    try:
        context = {}
        servings = int(request.GET.get('servings', 1))
        recep = DATA.get(dish)
        print(recep)
        final_dish = {}
        for dishs, caunt in recep.items():
            final_dish[dishs] = caunt * servings
            print(final_dish)
        context.setdefault('recipe', final_dish)
        return render(request,'calculator/index.html', context)
    except:
        context = {}
        return render(request, 'calculator/index.html', context)