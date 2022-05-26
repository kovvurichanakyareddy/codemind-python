n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(n):
    s+=l[i]
print(s)