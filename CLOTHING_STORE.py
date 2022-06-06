n=int(input())
p=0
arr=list(map(int,input().split()))
t=set(arr)
for i in t:
    c=0
    for j in range(n):
        if i==arr[j]:
            c+=1
    if c%2==0:
        p+=c//2
    else:
        if c>2:
            c-=1
            p+=c//2
print(p)