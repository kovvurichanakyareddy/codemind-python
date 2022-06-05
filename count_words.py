s=list(map(str,input().split()))
c=0
for i in range(len(s)):
    e=s[i]
    if e[0] in 'aeiouAEIOU' and e[len(e)-1] not in 'aeiouAEIOU':
        c+=1
print(c)