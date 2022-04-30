st=input()
n=len(st)
z=0
o=0
for i in range(0,n):
    if st[i]=='z':
        z+=1
    if st[i]=='o':
        o+=1
if 2*z==o:
    print("Yes")
else:
    print("No")