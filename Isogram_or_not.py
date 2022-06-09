s=input()
su=0
for char in s:
    c=0
    for chan in s:
        if char==chan:
            c+=1
    if c>1:
        su=1
        break
if su==0:
    print(True)
else:
    print(False)