n=int(input())
def add(n):
    s=0
    c=0
    while n>0:
        r=n%10
        c+=1
        s+=r
        n//=10
    if c==1:
        return s
    else:
        n=s
        return add(n)
print(add(n))