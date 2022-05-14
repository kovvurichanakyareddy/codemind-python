alice,bob=0,0
a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
for i in range(3):
    if a[i]>b[i]:
        alice+=1
    if a[i]<b[i]:
        bob+=1
print("%d %d"%(alice,bob))