from django.db import models

# Create your models here.


class Category(models.TextChoices):
    SHUMA = '新浪数码'
    KEJI = '新浪科技'
    IT = 'IT之家'
    KUAI = '快科技'
    PACIFIC = '太平洋电脑网'
    ZX = '中关村在线'
    JD = '中国家电网'
    CNMO = 'CNMO'
    MARKET = '市场资讯'
    RUN = '媒体滚动'
    KJZH = '新浪科技综合'
    PP = '澎湃新闻'
    CL = '财联社'
    K = '快科技2018'
    JM = '界面新闻'
    OTHER = '其他'

class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    intro = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=100)
    source = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)
    hotness = models.IntegerField()
    imgs_num = models.IntegerField()
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    



class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.CharField(max_length=10)
    comment_content =models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)