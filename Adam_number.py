def adam(n):
    rev,sr=0,0
    sq=n*n
    while n!=0:
        r=n%10
        rev=rev*10+r
        n//=10
    sq2=rev*rev
    while sq2!=0:
        r=sq2%10
        sr=sr*10+r
        sq2//=10
    if sq==sr:
        return True
    else:
        return False
n=int(input())
print(adam(n))