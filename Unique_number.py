n=int(input())
arr=[]
s,c,p=0,0,0
while n!=0:
    r=n%10
    arr.append(r)
    s+=1
    n//=10
for i in range(s):
    c=0
    for j in range(s):
        if arr[i]==arr[j]:
            c+=1
    if c>1:
        print('Not Unique Number')
        p+=1
        break
if p==0:
    print("Unique Number")