n=int(input())
arr=list(map(int,input().split()))
newarr=[]
for i in range(n):
    if i%2==0:
        for j in range(arr[i+1]):
            newarr.append(arr[i])
print(*newarr)