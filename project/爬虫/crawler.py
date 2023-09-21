import requests
import re
from bs4 import BeautifulSoup as BS
import json
import datetime

init_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2515&k=&num=50&page={}'
#init_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2515&etime=1647187200&stime=1647273600&ctime=1647273600&date=2022-03-14&k=&num=50&page={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    }

res = {}

def get_details(url):
    response2 = requests.get(url=url,params={},headers=headers)
    response2.encoding='utf-8'
    soup=BS(response2.text,'lxml')
    #正文文本
    content = []
    for p in soup.select('#artibody p'):
        content.append(p.text.strip())
    res['content'] = content
    
    #基本信息
    if soup.select('span.date') != []:
        res['date'] = soup.select('span.date')[0].contents[0]  #日期
    else:
        res['date'] = soup.select('#pub_date')[0].text.strip()



#得到一页的新闻
def get_news(i):
    page_i = requests.get(url=init_url.format(i),params={},headers=headers)
    page_i.encoding='utf-8'
    html = page_i.json()
    

    #item为每一个新闻
    for item in html['result']['data']:
        #网页URL
        res['url'] = item['url']
        with open('url.txt','a') as f2:
            f2.write(item['url']+'\n')
        #标题
        res['title'] = item['title']
        #简介
        res['intro'] = item['intro']
        #正文图片
        img =[]
        if len(item['images'])!=0:
            for i in item['images']:
                img.append(i['u'])
        res['img'] = img
        #作者和来源
        res['author'] = item['author']
        res['media_name'] = item['media_name']

        get_details(item['url'])
        #get_comments(item['url'])

        with open('result.txt','a',encoding='utf-8') as f3:
            f3.write(json.dumps(res, ensure_ascii=False))
            f3.write('\n')

#按页数爬取信息
for i in range(50):
    get_news(i)
    print("finished page {}".format(i))

#按照日期爬取
"""
start_date = datetime.date(2022,3,1)
end_date = datetime.date(2022,7,1)
current_date = start_date
while current_date <=end_date:
    date = current_date.strftime("%Y-%m-%d")
    init_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2515&etime=1669392000&stime=1669478400&ctime=1669478400&date=' + date +'&k=&num=50&page={}'
    get_news(1)
    current_date += datetime.timedelta(days=1)
    print("finished page",date) 
"""


print("finished")