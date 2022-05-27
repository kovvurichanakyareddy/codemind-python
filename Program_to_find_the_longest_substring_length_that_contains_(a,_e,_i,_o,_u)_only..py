s=input()
c,t=0,0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        c+=1
    else:
        if c>t:
            t=c
            c=0
print(t)