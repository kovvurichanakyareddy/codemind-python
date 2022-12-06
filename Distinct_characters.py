n=input()
n=n.lower()
l=[]
ll=[]
for i in n:
    if i not in l:
        if i!=" ":
            l.append(i)
for i in l:
    c=n.count(i)
    if c==1:
        ll.append(i)
ll.sort()
for i in ll:
    print(i,end='')