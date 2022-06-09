l=list(map(str,input().split()))
for i in l:
    print(ord(max(i))-ord(min(i)),end=' ')