from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import Game, Buyer


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'third_task/shop.html', context)


def cart(request):
    return render(request, 'third_task/cart.html')


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            existing_users = Buyer.objects.values_list('name', flat=True)
            if username in existing_users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return render(request, 'templates/third_task/registration_page.html',
                              {'info': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'third_task/registration_page.html', info)


class Menu(TemplateView):
    template_name = 'third_task/menu.html'
