import numpy as np
a=[]
b=[]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
arr = np.array(a)
brr = np.array(b)
cos = np.dot(arr,brr) / (np.linalg.norm(arr)*np.linalg.norm(brr))
print(f"{cos:.2f}")