n=int(input())
arr1=[]
arr2=[]
for i in range(0,n):
    a,b=map(int,input().split())
    arr1.append(a)
    arr2.append(b)
for i in range(0,n):
    co=0
    for j in range(arr1[i],arr2[i]+1):
        r=j%10
        if(r==2 or r==3 or r==9):
            co+=1
    print(co)