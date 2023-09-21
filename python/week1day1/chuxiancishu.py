n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
"""
num=[]
for i in arr:
    num.append(arr.count(i))
x=max(num)
for i in arr:
    if arr.count(i)==x:
        res=i
print(res)
"""
d={i:arr.count(i) for i in arr}
v=list(d.values())
key_list=list(filter(lambda k:d.get(k)==max(v),d.keys()))
print(key_list[0])

    