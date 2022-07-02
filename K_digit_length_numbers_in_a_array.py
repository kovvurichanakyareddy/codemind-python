n,k=map(int,input().split())
s=0
l=list(map(str,input().split()))
for i in l:
    c=0
    for char in i:
        if char!='-':
            c+=1
    if c==k:
        s+=1
print(s)       