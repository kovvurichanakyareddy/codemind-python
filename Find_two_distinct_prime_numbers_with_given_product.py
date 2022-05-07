n=int(input())
so=0
s=0
for i in range(1,n):
    if n%i==0:
        f=0
        for j in range(1,i+1):
            if i%j==0:
                f+=1
        if f==2:
            if so*i==n:
                s+=1
                print("%d %d"%(so,i))
                break
            so=i
if s==0:
    print("-1")