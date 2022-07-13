n=int(input())
if n==0 or n==1:
    print(True)
else:
    a=0
    b=1
    while(True):
        c=a+b
        if n==c:
            print(True)
            break
        if c>n:
            print(False)
            break
        a=b
        b=c
