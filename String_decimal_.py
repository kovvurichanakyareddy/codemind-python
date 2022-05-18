m=int(input())
for i in range(m):
    s=input()
    n=len(s)
    c=0
    for char in s:
        if char.isdigit():
            c+=1
    if(c==n):
        print(True)
    else:
        print(False)