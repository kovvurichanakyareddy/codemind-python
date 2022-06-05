n,m=map(int,input().split())
tar=[]
ln=list(map(int,input().split()))
lm=list(map(int,input().split()))
for i in lm:
    if i in ln:
        if i not in tar:
            tar.append(i)
print(len(tar))