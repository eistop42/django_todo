from django.shortcuts import render
from django.http import HttpResponse

from .models import Task, Product

todo = [
    {'id': 1, 'name': 'купить подарки'},
    {'id': 2, 'name': 'поставить елку'}

]

def main(request):

    # получить все задачи
    todo = Task.objects.all()

    status = request.GET.get('status')

    if status:
        # отфильтровать
        todo = todo.filter(status=status)

    # добавить новую задачу
    if request.method == 'POST':
        text_data = request.POST['text']
        descr_data = request.POST['descr']

        if text_data and descr_data:

            Task.objects.create(name=text_data, descr=descr_data)



    return render(request, 'main.html', {'todo': todo})


def about(request):
    return HttpResponse('<h2>разработка академии</h2>')

def products(request):

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']

        Product.objects.create(name=name, price=price)

    products = Product.objects.all()
    return render(request, 'products.html', {'my_products': products})


def task(request, task_id):

    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        # достали статус из запроса
        status = request.POST['status']

        # изменили статус у задачи в переменной task на тот, что в переменной status
        task.status = status

        # сохранили изменения в базу
        task.save()

    return render(request, 'task.html', {'task': task})

