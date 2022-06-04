n=int(input())
t=n-1
l=list(map(int,input().split()))
if n%2==0:
    for i in range(n//2):
        print(l[i],l[(n-1)-i],end=' ')
else:
    for i in range(n//2):
            print(l[i],l[(n-1)-i],end=' ')
    print("%d %d"%(l[n//2],0))
    