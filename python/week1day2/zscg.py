n,m=map(int,input().split())
kv={}
for i in range(n):
    x,y=input().split()
    kv[x]=y

for i in range(m):
    opp=input().split()
    if opp[0]=='Q':
        if opp[1] in kv.keys():
            print(kv[opp[1]])
        else:
            print(None)
    elif opp[0]=='A':
        kv[opp[1]]=opp[2]
    elif opp[0]=='D':
        if opp[1] in kv.keys():
            del kv[opp[1]]

sorted_kv=sorted(kv.items() , key=lambda x:x[0])
s_kv=dict(sorted_kv)
for i in s_kv.items():
    print(i[0],i[1])

"""
for i in range(m):
    if len(list(map(str,input().split())))==2:
        x,y=input().split()
        op.append(x)
        opp[y]=' '
        continue
    elif len(list(map(str,input().split())))==3:
        x,y,z=input().split()
        op.append(x)
        opp[y]=z
        continue
for x in op and y,z in opp.items():
    if x=='Q':
        if y in kv.keys():
            print(kv[y])
        else: print(None)
    elif x=='A':
        kv[y]=z
    elif x=='D':
        del kv[y]
"""

