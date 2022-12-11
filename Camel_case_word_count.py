string=input()
c=1
for i in range(1,len(string)-1):
    if string[i].isupper():
        c+=1
print(c)       