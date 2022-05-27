l=list(map(str,input().split()))
s=0
for i in range(len(l)):
    t1=l[i].lower()
    t2=t1[::-1]
    if(t1==t2):
        s+=1
print(s)