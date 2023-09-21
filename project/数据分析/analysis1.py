#数据处理
import json
from datetime import datetime
res = []
cleaned_res = []

with open('../project1/result.txt','r',encoding='utf-8') as f:
    for line in f:
        t = json.loads(line)
        pub_date = t['date']
        res.append(pub_date)

def clean_date_time(date_str):  
    try:   
        date_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')  
    except ValueError:  
        try:  
            date_time = datetime.strptime(date_str, '%Y年%m月%d日 %H:%M')  
        except ValueError:  
            try:  
                date_time = datetime.strptime(date_str, '%Y年%m月%d日%H:%M')  
            except ValueError:  
                return date_str  
  
    # 将时间戳转换为Django的DateTimeField格式  
    django_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')  
    return django_date_time

for i in res:
    cleaned_res.append(clean_date_time(i))

date_dict = {} #显示每天的新闻数
def res_append(st):
    if st not in date_dict:
        date_dict[st] = 1
    else: date_dict[st] +=1

for date_time in cleaned_res:
    date = date_time.split(' ')[0]
    res_append(date)

#画图
import matplotlib.pyplot as plt  
import matplotlib.dates as mdates  
 
dates = list(date_dict.keys())  
  
news_nums = list(date_dict.values())  
   
fig, ax = plt.subplots(figsize=(12,9))  
  
# 设置x轴为日期格式，并设置日期格式和日期分割  
fmt = mdates.DateFormatter('%Y-%m-%d')  
locator = mdates.DayLocator()  
ax.xaxis.set_major_formatter(fmt)  
ax.xaxis.set_major_locator(locator)  
 
ax.plot(dates, news_nums, 'o-')  
   
ax.set_xlabel('Date')   
ax.set_ylabel(r'News Number')  
  
plt.xticks(range(len(dates)), dates,rotation=60)
  
plt.savefig('news_num.jpg')   
plt.show()