from django.contrib import admin

from .models import Task, Product


admin.site.register(Task)
admin.site.register(Product)
