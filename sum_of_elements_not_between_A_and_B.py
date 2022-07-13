n=int(input())
c=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(n):
    if l[i]>b or l[i]<a:
        c+=l[i]
print(c)