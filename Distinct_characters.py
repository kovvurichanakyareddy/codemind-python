s=input()
s=s.lower()
l=[]
for ch in s:
    if ch.isalpha():
        if ch not in l:
            l.append(ch)
l.sort()
for i in l:
    print(i,end='')