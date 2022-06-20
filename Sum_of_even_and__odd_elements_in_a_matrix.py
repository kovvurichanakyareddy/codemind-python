a,b=map(int,input().split())
ev=[]
od=[]
for i in range(a):
    l=list(map(int,input().split()))
    for i in l:
        if i%2==0:
            ev.append(i)
        else:
            od.append(i)
print(sum(ev),sum(od))