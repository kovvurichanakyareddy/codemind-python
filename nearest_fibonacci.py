n=int(input())
a=0
b=1
while(True):
    c=a+b
    if c>n:
        fwd=c-n
        break
    bwd=n-c
    a=b
    b=c
if(fwd>bwd):
    print(n-bwd)
elif(fwd==bwd):
    print(n-bwd,n+fwd)
else:
    print(n+fwd)