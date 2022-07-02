n=int(input())
arr=[]
l=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==l[i]:
        arr.append(l[i])
        l[i]=0
if len(arr)!=0:
    print(min(arr),max(arr))
else:
    print(-1)