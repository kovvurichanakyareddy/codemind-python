s=input()
arr=[]
for c in s:
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
        arr.append(c)
n=(len(arr))-1
for c in s:
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
        print(arr[n],end='')
        n-=1
    else:
        print(c,end='')
    