a,b=map(int,input().split())
ev=od=0
for i in range(a):
    l=list(map(int,input().split()))
    if i%2==0:
        ev+=sum(l)
    else:
        od+=sum(l)
print(ev,od)