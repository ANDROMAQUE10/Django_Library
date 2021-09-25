from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthUserForm, RegisterUserForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить книгу", 'url_name': 'add_book'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]


def index(request):
    books = Book.objects.all()
    context = {'books': books,
               'menu': menu,
               'title': 'Каталог книг'
               }
    return render(request, 'catalog/index.html', context=context)


class LoginView(LoginView):
    template_name = 'catalog/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('catalog')


class RegisterView(CreateView):
    model = User
    template_name = 'catalog/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('catalog')
    success_msg = 'Пользователь создан'
