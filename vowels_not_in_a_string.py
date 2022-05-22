s=input()
a,e,i,o,u=0,0,0,0,0
for char in s:
    if char=='a':
        a+=1
    if char=='e':
        e+=1
    if char=='i':
        i+=1
    if char=='o':
        o+=1
    if char=='u':
        u+=1
if a==0:
    print('a',end=' ')
if e==0:
    print('e',end=' ')
if i==0:
    print('i',end=' ')
if o==0:
    print('o',end=' ')
if u==0:
    print('u',end=' ')
if a!=0 and e!=0 and i!=0 and o!=0 and u!=0:
    print(0)