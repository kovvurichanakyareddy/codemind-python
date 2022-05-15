s=input()
c=0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        c+=1
    if char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        c+=1
print(c)