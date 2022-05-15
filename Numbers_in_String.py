s=input()
su=0
for char in s:
    if char.isdigit():
        su+=int(char)
print(su)