n=int(input())
arr=[]
for s in range(0,n):
    e=int(input())
    arr.append(e)
for s in range(0,n):
    f=0
    frd=0
    bkd=0
    for i in range(arr[s]-1,0,-1):
        f=0
        for j in range(1,i+1):
            if i%j==0:
                f+=1
        if f==2:
            bkd=arr[s]-i
            break
    t=arr[s]
    while t>0:
        f=0
        for j in range(1,t+1):
            if t%j==0:
                f+=1
        if f==2:
            fwd=t-arr[s]
            break
        t+=1

    if fwd<bkd:
        print(t)
    else:
        print(i)