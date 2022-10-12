n=int(input())
l=list(map(int,input().split()))
c=0
t=0
for i in set(l):
    c=0
    for j in range(len(l)):
        if l[j]%i==0:
            c+=1
    if c==len(l):
        t=1
        print(i)
        break
if t==0:
    print(1)
