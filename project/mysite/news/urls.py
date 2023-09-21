from django.urls import path, include
from . import views

app_name = "news"
urlpatterns = [
    path('',views.index, name='index'),
    path('news_list/',views.news_list, name='news_list'),
    path('news/<int:news_id>', views.news_details, name='news_details'),
    path('comment/<int:news_id>', views.comment, name='comment'),
    path('delete_comment/<int:news_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('categories', views.category, name='category'),
    path('categories/<str:source>', views.cate_source, name='category_details'),
    path('search_results/', views.search, name='search_results'),

]