s=input()
s=s.lower()
l=[]
arr=[]
for ch in s:
    if ch.isalpha():
        l.append(ch)
for i in l:
    if l.count(i)==1:
        arr.append(i)
print(len(arr))