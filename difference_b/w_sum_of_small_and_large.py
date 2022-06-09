l=list(map(str,input().split()))
mi=ma=0
for i in l:
    mi+=ord(min(i))
    ma+=ord(max(i))
print(ma-mi)