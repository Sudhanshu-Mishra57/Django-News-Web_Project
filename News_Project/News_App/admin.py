from distutils.command import register
from django.contrib import admin
from News_App.models import News

# Register your models here.
admin.site.register(News)
