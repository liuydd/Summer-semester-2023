import torch
a = torch.tensor(list(map(int,input().split())))
b = torch.tensor(list(map(int,input().split())))
cos = (a.float()*b.float()).sum() / (torch.norm(a.float())*torch.norm(b.float()))
print(f"{cos:.2f}")