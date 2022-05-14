a=int(input())
l1=list(map(int,input().strip().split()))
b=int(input())
l2=list(map(int,input().strip().split()))
c=int(input())
s=0
for i in range(a):
    if l1[i]<=c and l2[i]>=c:
        s+=1
print(s)