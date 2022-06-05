n,m=map(int,input().split())
nl=list(map(int,input().split()))
ml=list(map(int,input().split()))
for i in nl:
    if i not in ml:
        print(i,end=' ')
for i in ml:
    if i not in nl:
        print(i,end=' ')