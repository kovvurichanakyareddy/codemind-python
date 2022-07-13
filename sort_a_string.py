s=input()
ar=[]
for ch in s:
    if ch.isalpha() or ch.isdigit():
        ar.append(ch)
ar.sort()
i=0
for ch in s:
    if ch.isalpha() or ch.isdigit():
        print(ar[i],end='')
        i+=1
    else:
        print(ch,end='')