a=int(input())
b=int(input())
for i in range(a,b+1):
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f+=1
    if f==2:
        print(i)