n=int(input())
l=list(map(int,input().strip().split()))
for i in range(n):
    s=0
    for j in range(n):
        if l[i]>l[j]:
            s+=1
    print(s,end=' ')