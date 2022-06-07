n=int(input())
arr=list(map(int,input().split()))
temp=[]
for i in arr:
    if i not in temp:
        temp.append(i)
for i in temp:
    c=0
    for j in range(n):
        if i==arr[j]:
            c+=1
    print(i,c,end=' ')