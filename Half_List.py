n=int(input())
arr=[]
l=list(map(int,input().strip().split()))
for i in range(n):
    arr.append(l[i])
for i in range(n-1,n//2-1,-1):
    print(arr[i],end=' ')
for i in range(0,n//2):
    print(arr[i],end=' ')