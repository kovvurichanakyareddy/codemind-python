s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
s=0
for ch in s1:
    if ch not in s2:
        s=1
if s==0:
    print(True)
else:
    print(False)