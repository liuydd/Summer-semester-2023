import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
m1,m2,n,a,b = map(int,input().split())
a_data, a_col, a_row = [], [], []
for _ in range(a):
    i,j,k = map(int, input().split())
    a_data.append(k)
    a_row.append(i-1)
    a_col.append(j-1)
A = csr_matrix((a_data,(a_row,a_col)),shape=(m1,n))
b_data, b_col, b_row = [], [], []
for _ in range(b):
    i,j,k = map(int, input().split())
    b_data.append(k)
    b_row.append(i-1)
    b_col.append(j-1)
B = csr_matrix((b_data,(b_row,b_col)),shape=(m2,n))
s = cosine_similarity(A,B)
c, d = np.unravel_index(np.argmax(s),s)
print(c+1, d+1)
