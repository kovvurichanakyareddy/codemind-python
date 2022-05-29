n=int(input())
l=list(map(int,input().split()))
X,Y=0,0
for i in range(n):
    if i%2==0:
        X+=l[i]
    else:
        Y+=l[i]
ans=X-Y
if ans<0:
    ans*=(-1)
if ans%4==0:
    print('X')
else:
    print('Y')
    