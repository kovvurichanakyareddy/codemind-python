s=input()
l=[]
for ch in s:
    l.append(ch)
for i in l:
    if l.count(i)==1:
        print(i)
        break
else:
    print(-1)