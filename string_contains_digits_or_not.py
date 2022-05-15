n=int(input())
arr=[]
for i in range(n):
    e=input()
    arr.append(e)
    s=0
    for char in arr[i]:
        if char.isdigit():
            s+=1
    if s==0:
        print("No")
    else:
        print("Yes")