# Generated by Django 5.1.4 on 2024-12-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='descr',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]