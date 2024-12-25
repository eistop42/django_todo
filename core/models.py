from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    descr = models.TextField(verbose_name='Описание', blank=True, null=True)


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name



