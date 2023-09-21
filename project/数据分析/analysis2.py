import json
from datetime import datetime
res = []
cleaned_res = []
source = []
cate = ['新浪数码', '新浪科技', 'IT之家', '快科技', '太平洋电脑网', '中关村在线', '中国家电网', 'CNMO', '市场资讯', '媒体滚动', '新浪科技综合', '澎湃新闻', '财联社', '快科技2018', '界面新闻', '其他']

with open('../project1/result.txt','r',encoding='utf-8') as f:
    for line in f:
        t = json.loads(line)
        pub_date = t['date']
        if t['author'] !='':
            author = t['author']
        else: author = t['media_name']
        if author in cate:
            source.append(author)
        else: source.append('其他')
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

#按分类来构建新字典
dict_1,dict_2,dict_3,dict_4,dict_5,dict_6,dict_7,dict_8,dict_9,dict_10,dict_11,dict_12,dict_13,dict_14,dict_15,dict_16 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

for i in range(len(source)):
    if source[i]=='新浪数码': dict_1.append(cleaned_res[i])
    elif source[i]=='新浪科技': dict_2.append(cleaned_res[i])
    elif source[i]=='IT之家': dict_3.append(cleaned_res[i])
    elif source[i]=='快科技': dict_4.append(cleaned_res[i])
    elif source[i]=='太平洋电脑网': dict_5.append(cleaned_res[i])
    elif source[i]=='中关村在线': dict_6.append(cleaned_res[i])
    elif source[i]=='中国家电网': dict_7.append(cleaned_res[i])
    elif source[i]=='CNMO': dict_8.append(cleaned_res[i])
    elif source[i]=='市场资讯': dict_9.append(cleaned_res[i])
    elif source[i]=='媒体滚动': dict_10.append(cleaned_res[i])
    elif source[i]=='新浪科技综合': dict_11.append(cleaned_res[i])
    elif source[i]=='澎湃新闻': dict_12.append(cleaned_res[i])
    elif source[i]=='财联社': dict_13.append(cleaned_res[i])
    elif source[i]=='快科技2018': dict_14.append(cleaned_res[i])
    elif source[i]=='界面新闻': dict_15.append(cleaned_res[i])
    elif source[i]=='其他': dict_16.append(cleaned_res[i])

date_dict = {} #显示每天的新闻数
def res_append(st):
    if st not in date_dict:
        date_dict[st] = 1
    else: date_dict[st] +=1

#以第一分类为例，其他分类类似
for date_time in dict_1:
    date = date_time.split(' ')[0]
    res_append(date)

import matplotlib.pyplot as plt  
import matplotlib.dates as mdates  

  
# 将字典的键转换为列表，以便作为x轴的值  
dates = list(date_dict.keys())  
  
# 将字典的值转换为列表，以便作为y轴的值  
news_nums = list(date_dict.values())  
  
# 创建figure和axes对象  
fig, ax = plt.subplots(figsize=(12,9))  
  
# 设置x轴为日期格式，并设置日期格式和日期分割  
fmt = mdates.DateFormatter('%Y-%m-%d')  
locator = mdates.DayLocator()  
ax.xaxis.set_major_formatter(fmt)  
ax.xaxis.set_major_locator(locator)  

# 使用plot函数绘制数据  
ax.plot(dates, news_nums, 'o-')  
  
# 设置x轴的标签和标题  
ax.set_xlabel('Date')  
# 设置y轴的标签为新闻数量  
ax.set_ylabel(r'News Number')  

plt.xticks(range(len(dates)), dates,rotation=60)

# 保存图像为'news_num_cate1.jpg'文件  
plt.savefig('news_num_cate1.jpg')  
# 显示图形  
plt.show()