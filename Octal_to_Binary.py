n=int(input())
for i in range(n):
    x=int(input())
    t=0
    d=0
    while(x>0):
        r=x%10
        d+=(8**t)*r
        t+=1
        x=x//10
    print(bin(d)[2:])