from django.contrib import admin

# Register your models here.
from news.models import Category, News, Comment

class Article_Modeladmin(admin.ModelAdmin):
    list_display = ['title','author','pub_date','intro']  #这里的评论数没有列出来

#admin.site.register(Category)
admin.site.register(News, Article_Modeladmin)
admin.site.register(Comment)