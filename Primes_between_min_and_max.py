n=int(input())
t=1
c=0
l=list(map(int,input().split()))
mi=l.index(min(l))
ma=l.index(max(l))
if mi>ma:
    t=-1
for i in range(mi,ma+1,t):
    f=0
    for j in range(1,l[i]):
        if l[i]%j==0:
            f+=1
    if f==1:
        c+=1
print(c)