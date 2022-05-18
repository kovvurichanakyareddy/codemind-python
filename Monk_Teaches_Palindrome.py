n=int(input())
for i in range(n):
    s=input()
    su=len(s)
    if s==s[::-1]:
        print('YES',end=' ')
        if su%2==0:
            print('EVEN')
        else:
            print('ODD')
    else:
        print('NO')