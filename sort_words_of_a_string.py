l=list(map(str,input().split()))
for i in range(len(l)):
    s=l[i]
    ar=[]
    for char in s:
        if char.isalpha():
            ar.append(char)
    ar.sort()
    t=0
    for nc in s:
        if nc.isalpha():
            print(ar[t],end='')
            t+=1
        else:
            print(nc,end='')
    ar.clear()
    print(' ',end='')