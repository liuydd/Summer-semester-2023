import json
import django
import os
import random
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django.setup()

def clean_date_time(date_str):  #统一日期时间格式
    try:   
        date_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')  
    except ValueError:  
        try:  
            date_time = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M')  
        except ValueError:  
            try:  
                date_time = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M:%S')  
            except ValueError:  
                return date_str  
  
    # 将时间戳转换为Django的DateTimeField格式  
    django_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')  
    return django_date_time

def main():
    from news.models import News
    with open('result.txt','r',encoding='utf-8') as f:
        for line in f:
            t = json.loads(line)
            link = t['url']
            title = t['title']
            if t['author'] !='':
                author = t['author']
            else: author = t['media_name']
            pub_date = clean_date_time(t['date'])
            intro = t['intro']
            content = ''
            for p in t['content']:
                content +=p
                content+='\n'
            cate = ['新浪数码', '新浪科技', 'IT之家', '快科技', '太平洋电脑网',  '中关村在线', '中国家电网', 'CNMO', '市场资讯', '媒体滚动', '新浪科技综合', '澎湃新闻', '财联社', '快科技2018', '界面新闻', '其他']
            if author in cate:
                #category =  Category.objects.create(name = author)
                source = author
            else: #category =  Category.objects.create(name = '其他')
                source = '其他'
            hotness = random.randint(100,100000)
            imgs_num = len(t['img'])
            News.objects.create(title = title, author = author, pub_date = pub_date, intro = intro, content = content, link = link, source = source, hotness=hotness, imgs_num = imgs_num)

if __name__ == "__main__":
    main()
    print('Finished')
        

