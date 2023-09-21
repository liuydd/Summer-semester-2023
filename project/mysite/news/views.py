from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from news.models import Category, News, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import time
# Create your views here.

def index(request):
    random_news_list = News.objects.order_by('?')[:20]
    return render(request, 'news/index.html', {'random_news_list' : random_news_list})

def news_list(request):
    news = News.objects.all()
    paginator = Paginator(news, 50) #每页50条新闻
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    return render(request, 'news/news_list.html', { 'news_list': page_obj})

def turn(request):
    page_number = request.GET.get("page")
    if page_number:
        return redirect('news_list', page = page_number)

def news_details(request, news_id):
    news = get_object_or_404(News, pk = news_id) #pk为主键
    comments = news.comment_set.all().order_by('-create_time')
    comment_count = comments.count()
    news.comment_count = comment_count
    loop = range(news.imgs_num)
    n = news_id-7
    return render(request, 'news/news_details.html', {'news' : news, 'news_id' : news_id, 'comments' : comments, 'loop' : loop, 'n' : n})


def comment(request, news_id):
    data = request.POST
    user = data['user']
    comment_content = data['content']
    news = News.objects.get(id=news_id)
    news.comment_count +=1
    obj = Comment(news=news, user=user, comment_content=comment_content)
    obj.full_clean()
    obj.save()
    news.save()
    return HttpResponseRedirect(f'/news/{news_id}')

def delete_comment(request, news_id, comment_id):
    comment = get_object_or_404(Comment, news_id = news_id, id = comment_id)
    comment.delete()
    news = News.objects.get(id=news_id)
    news.comment_count -=1
    news.save()
    return HttpResponseRedirect(f'/news/{news_id}')

def category(request):
    count_res = []
    for category in Category:
        count = News.objects.filter(source = category).count()
        count_res.append(count)
    context = zip(Category, count_res)
    return render(request, 'news/category.html', {'categories' : context})


def cate_source(request,source): #展示具体来源的新闻
    news = News.objects.filter(source = source)
    paginator = Paginator(news, 50) #每页50条新闻
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj =paginator.page(paginator.num_pages)
    return render(request, 'news/category_details.html', {'news_list' : page_obj})

def turn2(request):
    page_number = request.GET.get("page")
    if page_number:
        return redirect('category_details', page = page_number)

def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        sorting = request.GET.get('sorting', 'time')
        categories = request.GET.getlist('categories')
        start_time = time.time()
        news_list = News.objects.filter(
            Q(title__icontains = keyword) | Q(content__icontains = keyword)
        )
        if sorting == 'hotness':
            news_list = news_list.order_by('-hotness')
        else: news_list = news_list.order_by('-pub_date')
        if categories:
            news_list = news_list.filter(source__in = categories)
        end_time = time.time()
        search_time = end_time - start_time
        paginator = Paginator(news_list, 50) #每页50条新闻
        page_number = request.GET.get("page")
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj =paginator.page(paginator.num_pages)
        context = {
        'time' : search_time,
        'news_list' : page_obj,
        'count' : len(news_list),
        'keyword' : keyword,
        'sorting' : sorting,
        'categories' : categories,
        }
        return render(request, 'news/search_results.html', context)
    else: return render(request, 'news/index.html')
        
    
    
