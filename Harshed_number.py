n=int(input())
s=0
temp=n
while temp>0:
    r=temp%10
    s+=r
    temp//=10
if n%s==0:
    print("True")
else:
    print("False")