n=int(input())
o,e=0,0
l=list(map(int,input().strip().split()))
for i in range(n):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if e-o==0:
    print("YES")
else:
    print("NO")