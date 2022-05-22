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

if a!=0 and e!=0 and i!=0 and o!=0 and u!=0:
    print(True)
else:
    print(False)