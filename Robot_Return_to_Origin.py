s=input()
su=0
for ch in s:
    if ch=='U':
        su+=1
    if ch=='D':
        su-=1
    if ch=='R':
        su+=2
    if ch=='L':
        su-=2
if su==0:
    print(True)
else:
    print(False)