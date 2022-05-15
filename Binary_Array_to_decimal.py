def binary(n):
    r=0
    i=0
    while n:
        rem=n%10
        r+=((2**i)*rem)
        n//=10
        i+=1
    return r
n=int(input())
l=list(map(int,input().strip().split()))
num=0
for i in range(n):
    num=num*10+l[i]
print(binary(num))