import numpy as np
t=int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    ar=np.arange(n*m)
    arr=ar.reshape(n,m)
    for i in range(n):
        arr[i]=list(map(int,input().split()))
    #temp=arr[0].copy()
    #arr[0],arr[n-1]=arr[n-1],temp
    arr[[0,n-1],:] = arr[[n-1,0],:]
    arr[:,[0,m-1]] = arr[:,[m-1,0]]
    arrr=arr.astype('bool')
    arrr=~arrr
    arrr=arrr.astype('int')
    for i in range(n):
        for j in range(m):
            print(arrr[i][j],end=' ')
        print()
