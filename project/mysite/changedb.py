import json
from datetime import datetime
import random
res = []
cleaned_res = []
img_res = []

with open('result.txt','r',encoding='utf-8') as f:
    for line in f:
        t = json.loads(line)
        pub_date = t['date']
        res.append(pub_date)
        img = t['img']
        img_res.append(len(img))

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

import sqlite3  
# 连接到数据库  
conn = sqlite3.connect('db.sqlite3')  

# 创建一个游标对象  
cursor = conn.cursor()  
cursor.execute("SELECT id, hotness, imgs_num, pub_date FROM news_news") 
rows = cursor.fetchall() 

for row in rows:
    hot = random.randint(100,100000)
    cursor.execute("UPDATE news_news SET hotness = ? , imgs_num = ?  ,pub_date = ? WHERE id = ?", (hot,img_res[row[0]-7],cleaned_res[row[0]-7],row[0]))
    conn.commit()  

conn.close()