n=int(input())
a1=list(map(str,input().split()))
a2=[]
for i in range(0,n):
    a2.append(len(a1[i]))
for i in range(n):
    if a2[i]==max(a2):
        print(a1[i],end=' ')