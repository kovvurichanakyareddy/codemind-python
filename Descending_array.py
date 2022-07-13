n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n):
    r.append(l[i])
r.sort(reverse=True)
if l==r:
    print("yes")
else:
    print("no")