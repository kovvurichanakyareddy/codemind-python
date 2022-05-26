n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    st=0
    for j in range(min(l),max(l)+1):
        c=0
        for k in range(len(l)):
            if j==l[k]:
                c=1
        if c==0:
            print(j)
            st=1
    if st==0:
        print(max(l)+1)
            