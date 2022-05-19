n=int(input())
su,c,d=0,0,0
arr=list(map(int,input().strip().split()))
for i in range(n):
    su=0
    for j in range(n):
        if arr[i]==arr[j]:
            su+=1
    if su==arr[i]:
        d+=1
        arr[i]=0
print(d)