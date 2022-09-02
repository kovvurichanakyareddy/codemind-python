s1=input()
s2=input()
l=[]
for ch in s1:
    l.append(ch)
for ch in s2:
    l.append(ch)
l.sort()
for i in l:
    print(i,end='')
