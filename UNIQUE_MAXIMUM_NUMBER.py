n=int(input())
l=list(map(int,input().strip().split()))
c,s,t=0,0,0
for i in range(n):
    s=0
    for j in range(n):
        if l[i]==l[j]:
            s+=1
    if s==1:
        if l[i]>t:
            t=l[i]
            c+=1
if c!=0:
    print(t)
else:
    print("-1")