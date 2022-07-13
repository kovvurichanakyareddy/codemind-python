s=input()
c=0
for ch in s:
    if  not(ch.isalpha() or ch.isdigit() or ch==' '):
        c+=1
print(c)