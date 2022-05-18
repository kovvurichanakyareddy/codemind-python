s=input()
se=input()
su=0
for char in s:
    if char==se:
        su+=1
if su>0:
    print(su)
else:
    print('-1')