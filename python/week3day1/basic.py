import torch
t=int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    arr = torch.zeros(n,m,dtype=bool)
    for i in range(n):
        arr[i] = torch.tensor(list(map(int,input().split())))
    arr[[0,n-1],:] = arr[[n-1,0],:]
    arr[:,[0,m-1]] = arr[:,[m-1,0]]
    arr=~arr
    for i in range(n):
        for j in range(m):
            print(int(arr[i][j]),end=' ')
        print()
