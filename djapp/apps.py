from django.apps import AppConfig


class DjappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djapp'


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '图书管理'