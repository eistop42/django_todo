from django.urls import path

from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('task/<int:task_id>', task, name='task_detail'),
    path('aboutpage', about),
    path('products', products)
]