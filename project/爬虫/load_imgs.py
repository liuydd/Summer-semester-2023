import requests
import json

def load_imgs(url, line_num, img_num):
    response = requests.get(url)
    with open('news{}_img{}.png'.format(line_num, img_num),'wb') as fp:
        fp.write(response.content)

with open('../result.txt','r',encoding='utf-8') as f:
    line_num = 0
    for line in f:
        t = json.loads(line)
        img = t['img']
        for url in img:
            load_imgs(url, line_num, img.index(url))
        print("finished news {}".format(line_num))
        line_num+=1

print('finished')
        