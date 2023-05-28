from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.template import loader
from .models import *
from .forms import *


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def about_me(request):
    return render(request, 'aboutme.html')


def products(request):
    template = loader.get_template('products.html')
    context = {
        'products': Product.objects.all(),
        'title': 'Список продуктов',
        'power_user': request.user.groups.filter(name='TEST').exists()
    }
    return HttpResponse(template.render(context, request))


def new_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('products'))
        else:
            form = ProductForm()
        template = loader.get_template('product_form.html')
        context = {
            'form': form,
            'title': 'добавление продукта'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1> Доступ запрещен</h1>")


def edit_product(request, kp):
    if request.user.is_authenticated:
        try:
            product = Product.objects.get(id=kp)
        except Product.DoesNotExist:
            raise Http404("Продукт с кодом" + str(kp) + " не найден")

        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('products'))
        else:
            form = ProductForm(instance=product)

        template = loader.get_template('product_form.html')
        context = {
            'form': form,
            'title': 'редактирование продукта'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1> Доступ запрещен</h1>")


def del_product(request, kp):
    if request.user.is_authenticated:
        try:
            product = Product.objects.get(id=kp)
        except Product.DoesNotExist:
            raise Http404("Продукт с кодом" + str(kp) + " не найден")
        m = f"Продукт {product.name} удален"
        product.delete()
        messages.error(request, m)
        return HttpResponseRedirect(reverse('products'))
    else:
        return HttpResponseForbidden("<h1> Доступ запрещен</h1>")


def dishes(request):
    template = loader.get_template('dishes.html')
    context = {
        'dishes': Dish.objects.all(),
        'title': 'Список блюд'
    }
    return HttpResponse(template.render(context, request))


def dish(request, dk):
    try:
        dish = Dish.objects.get(id=dk)
    except Dish.DoesNotExist:
        raise Http404("Блюдо с кодом" + str(dk) + " не найдено")

    template = loader.get_template('dish.html')
    context = {
        'dish': dish,
        'title': dish.name
    }
    return HttpResponse(template.render(context, request))


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    template = loader.get_template('user_form.html')
    context = {
        'form': form,
        'title': 'Создание пользователя'
    }
    return HttpResponse(template.render(context, request))


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=username, password=userpass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = AuthenticationForm()
    template = loader.get_template('user_form.html')
    context = {
        'form': form,
        'title': 'Вход в систему'
    }
    return HttpResponse(template.render(context, request))



def logout_user(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return HttpResponseRedirect(reverse('index'))
