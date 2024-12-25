from django.shortcuts import render
from django.http import HttpResponse

from .models import Task, Product

todo = [
    {'id': 1, 'name': 'купить подарки'},
    {'id': 2, 'name': 'поставить елку'}

]

def main(request):

    print(request.POST)
    todo = Task.objects.all()
    return render(request, 'main.html', {'todo': todo})


def about(request):
    return HttpResponse('<h2>разработка академии</h2>')

def products(request):
    products = [
        {'id': 1, 'name': 'батон', 'price': 100},
        {'id': 2, 'name': 'молоко', 'price': 50},
        {'id': 3, 'name': 'масло', 'price': 500},
    ]
    products = Product.objects.filter(price__lt=200, name='хлеб ')
    return render(request, 'products.html', {'my_products': products})


def task(request, task_id):

    task = Task.objects.get(id=task_id)

    return render(request, 'task.html', {'task': task})

