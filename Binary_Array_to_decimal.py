n=int(input())
t=0
c=0
l=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    c+=(2**t)*l[i]
    t+=1
print(c)