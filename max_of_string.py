s=input()
t='A'
for char in s:
    if ord(char)>ord(t):
        t=char
print(t)