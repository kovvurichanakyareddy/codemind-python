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
    tema=[]
    for i in l:
        arr.append(i[t2])
    t2+=1
    for i in range(len(arr)):
        tema.append(arr[i])
    tema.sort(reverse=True)
    if arr==sorted(arr):
        ma+=1
    if arr==tema:
        ma+=1
print(ma)