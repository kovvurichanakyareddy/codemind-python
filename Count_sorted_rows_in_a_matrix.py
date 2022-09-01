a,b=map(int,input().split())
c=0
for i in range(a):
    l=list(map(int,input().split()))
    t=[]
    for j in range(len(l)-1,-1,-1):
        t.append(l[j])
    t.sort(reverse=True)
    if l==sorted(l):
        c+=1
    if l==t:
        c+=1
print(c)