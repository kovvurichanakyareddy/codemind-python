s=input()
su=0
for c in s:
    if(c.isupper() or c.islower() or c.isdigit() or c==' '):
        continue
    su+=1
print(su)