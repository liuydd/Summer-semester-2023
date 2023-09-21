#backet sort

cit=list(map(int,input().split()))
citt=sorted(cit)
for i in range(len(citt),0,-1):
    if citt[-i]>=i:
        print(i)
        break
