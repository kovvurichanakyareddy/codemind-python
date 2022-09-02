a,b=map(int,input().split())
l=[]
for e in range(a):
    sl=list(map(int,input().split()))
    l.append(sl)
t=b-1
t2=0
ma=0
while t2<=t:
    arr=[]
    for i in l:
        arr.append(i[t2])
    t2+=1
    print(max(arr))
    