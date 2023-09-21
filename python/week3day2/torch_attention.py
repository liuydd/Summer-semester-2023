import os
os.environ["OMP_NUM_THREADS"] = "1"
#感觉这题的输入有点难想
import torch
q_shape = list(map(int, input().split()))
q = torch.tensor([list(map(float, input().split())) for _ in range(q_shape[0]*q_shape[1])]).reshape(q_shape)
k_shape = list(map(int, input().split()))
k = torch.tensor([list(map(float, input().split())) for _ in range(k_shape[0]*k_shape[1])]).reshape(k_shape)
v_shape = list(map(int, input().split()))
v = torch.tensor([list(map(float, input().split())) for _ in range(v_shape[0]*v_shape[1])]).reshape(v_shape)
t = torch.matmul(q,k.transpose(-2,-1))/(k.shape[-1]**0.5)
attention = torch.matmul(torch.softmax(t,dim=-1),v)
for row in attention.view(-1,attention.shape[-1]):
    print(' '.join([format(elem.item(), ".2f") for elem in row]))
