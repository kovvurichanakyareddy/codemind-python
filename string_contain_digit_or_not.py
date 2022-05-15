string=input()
s=0
for char in string:
    if char.isdigit():
        s+=1
if s!=0:
    print("Contains %d digit"%s)
else:
    print("Doesn't contain digit")