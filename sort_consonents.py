s=list(map(str,input().split()))
for i in range(len(s)):
    e=s[i]
    arr=[]
    for ch in e:
        if ch not in 'aeiou':
            arr.append(ch)
    t=0
    arr.sort()
    for ch in e:
        if ch not in 'aeiou':
            print(arr[t],end='')
            t+=1
        else:
            print(ch,end='')
    print(end=' ')