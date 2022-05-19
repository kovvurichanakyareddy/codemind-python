n=int(input())
l=list(map(int,input().strip().split()))
mi,ma,c=9,0,0
for i in range(n):
    s=0
    for j in range(n):
        if l[i]==l[j]:
            s+=1
    if s==l[i]:
        c+=1
        if l[i]<mi:
            mi=l[i]
        if l[i]>ma:
            ma=l[i]
        l[i]=0
if c>0:
    print("%d %d"%(mi,ma))
else:
    print('-1')