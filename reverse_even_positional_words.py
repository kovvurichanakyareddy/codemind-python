l=list(map(str,input().split(' ')))
for c in range(len(l)):
    if c%2==0:
        print(l[c][::-1],end=' ')
    else:
        print(l[c],end=' ')