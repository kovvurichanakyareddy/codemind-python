s=input()
s=s.lower()
arr=[]
for ch in s:
    if ch not in arr:
        if ch.isalpha():
            arr.append(ch)
arr.sort()
for i in arr:
    print(i,end='')