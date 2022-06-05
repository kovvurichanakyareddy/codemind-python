m,n=map(int,input().split())
temp=[]
ml=list(map(int,input().split()))
nl=list(map(int,input().split()))
for i in ml:
    if i not in temp:
        temp.append(i)
ml=temp
for i in ml:
    if i in nl:
        print(i,end=' ')