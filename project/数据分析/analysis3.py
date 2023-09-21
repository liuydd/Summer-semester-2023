import json
from datetime import datetime
res = []
cleaned_res = []
title_res = []
content_res = []

with open('../project1/result.txt','r',encoding='utf-8') as f:
    for line in f:
        t = json.loads(line)
        pub_date = t['date']
        title = t['title']
        content = ''
        for p in t['content']:
            content +=p
            content+='\n'
        res.append(pub_date)
        title_res.append(title)
        content_res.append(content)

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

#得到这三天的index
date_index_0823 = []
date_index_0302 = []
date_index_0314 = []

for date_time in cleaned_res:
    date = date_time.split(' ')[0]
    if date == '2023-08-23':
        date_index_0823.append(cleaned_res.index(date_time))
    elif date == '2022-03-02':
        date_index_0302.append(cleaned_res.index(date_time))
    elif date == '2022-03-14':
        date_index_0314.append(cleaned_res.index(date_time))

#分析2023-08-23
tit = []
con = []
for i in date_index_0823:
    tit.append(title_res[i])
    con.append(content_res[i])

import jieba

words = []
for t in tit:
    devision_t = jieba.cut(t,cut_all=False)
    words.extend(list(devision_t))

import re
stop_list = []
no_stop_words = []
for line in open("cn_stopwords.txt", 'r', encoding='utf-8').readlines():
    stop_list.append(line.strip())

for word in words:                                                  
    if word not in stop_list:                                      
        word = re.sub(r'\d', "", word)                               
        word = re.sub(r'\s', "", word)                               
        word = re.sub(r'\W', "", word)                               
        if word:
            no_stop_words.append(word)

result = {} 
def res_append(st):
    if st not in result:
        result[st] = 1
    else: result[st] +=1

for i in no_stop_words: res_append(i)

result = sorted(result.items(),  key=lambda kv:(kv[1], kv[0]), reverse=True)
result = dict(result)
new_a = {}
#输出所用次数最多的前十个
print("所用次数最多的前十个词")
for i, (k, v) in enumerate(result.items()):
    new_a[k] = v
    if i == 9:
        print(new_a)
        break

sum = 0
for i in result.values(): sum+=i
new_a2 = {}
for i in new_a.items():
    new_a2[i[0]] = i[1]/sum
print("所用次数最多的前十个词的词频")
print(new_a2)

#画图
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

# make data:
x = new_a2.keys()
y = list(new_a2.values())

# plot
fig, ax = plt.subplots(figsize=(13,10))


ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
 
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置默认字体为SimHei  
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

ax.set_xlabel('Word')   
ax.set_ylabel(r'Word Frequency')  

fig.tight_layout() 
  
plt.savefig('words_freq_0823.jpg')  
  
plt.show()