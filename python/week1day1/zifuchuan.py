a=input()
b=input()
a_=set(a)
b_=set(b)
res=a_-b_
l=list(res)
l.sort()
for i in l:
    print(i,end=' ')