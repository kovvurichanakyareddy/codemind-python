s=input()
v,c,d,w=0,0,0,0
for char in s:
    if char==' ':
        w+=1
    elif char.isdigit():
        d+=1
    elif char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        v+=1
    elif char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        v+=1
    elif char!='a' and char!='e' and char!='i' and char!='o' and char!='u':
        c+=1
    elif char!='A' and char!='E' and char!='I' and char!='O' and char!='U':
        c+=1
print("Vowels: %d"%v)
print("Consonants: %d"%c)
print("Digits: %d"%d)
print("White spaces: %d"%w)