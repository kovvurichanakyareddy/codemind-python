a,b=map(int,input().split())
arr=[]
for i in range(a):
    l=list(map(int,input().split()))
    arr.append(sum(l))
print(max(arr))