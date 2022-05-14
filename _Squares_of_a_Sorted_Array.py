n=int(input())
arr=[]
l=list(map(int,input().strip().split()))
for i in range(n):
    arr.append(l[i]**2)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(n):
    print(arr[i],end=' ')