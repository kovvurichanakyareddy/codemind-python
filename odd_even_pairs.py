n=int(input())
ev=[];od=[]
l=list(map(int,input().split()))
for i in range(n):
    if l[i]%2==0:
        ev.append(l[i])
    else:
        od.append(l[i])
while True:
    if len(od)>0:
        print(od[0],end=' ')
        od.remove(od[0])
    if len(ev)>0:
        print(ev[0],end=' ')
        ev.remove(ev[0])
    if len(ev)==0 and len(od)==0:
        break
if n%2!=0:
    print(0)