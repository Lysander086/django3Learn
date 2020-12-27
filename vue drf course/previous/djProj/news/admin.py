from django.contrib import admin

# Register your models here.

from .models import Article, Journalist

admin.site.register(Article)
admin.site.register(Journalist)