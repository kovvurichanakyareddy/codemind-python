n=int(input())
a1=list(map(str,input().split()))
a2=[]
for i in range(0,n):
    a2.append(len(a1[i]))
print(a2.count(max(a2)))