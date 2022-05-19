n=int(input())
su,d=0,0
arr=list(map(int,input().strip().split()))
k=int(input())
for i in range(n):
    su=0
    for j in range(n):
        if arr[i]==arr[j]:
            su+=1
    if su==k:
        print(arr[i],end=' ')
        d+=1
        arr[i]=0
if d==0:
    print('-1')