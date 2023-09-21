n=int(input())
arr=[]
arr=list(map(int,input().split()))
tar=int(input())
for a in arr:
    for b in arr[arr.index(a)+1:]:
        if b==tar-a:
            print(arr.index(a),arr.index(b))