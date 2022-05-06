n=int(input())
f=0
frd=0
bkd=0
for i in range(n-1,0,-1):
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f+=1
    if f==2:
        bkd=n-i
        break
t=n
while t>0:
    f=0
    for j in range(1,t+1):
        if t%j==0:
            f+=1
    if f==2:
        fwd=t-n
        break
    t+=1
if fwd==0 and bkd==0:
    print("0")
elif fwd<bkd:
    print(fwd)
else:
    print(bkd)