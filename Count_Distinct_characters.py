s=input()
s=s.lower()
arr=[]
for ch in s:
    if ch not in arr:
        if ch.isalpha():
            arr.append(ch)
print(len(arr))