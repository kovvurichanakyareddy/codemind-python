s=input()
arr=[]
mi=ma=0
for char in s:
    if char.isalpha():
        arr.append(ord(char))
for i in arr:
    if i==min(arr):
        mi+=1
    if i==max(arr):
        ma+=1
print(chr(min(arr)),mi,chr(max(arr)),ma)