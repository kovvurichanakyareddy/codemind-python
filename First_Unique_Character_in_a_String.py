s=input()
c=0
for char in s:
    si=0
    for chare in s:
        if char==chare:
            si+=1
    if si==1:
        print(s.index(char))
        c+=1
        break
if c==0:
    print('-1')