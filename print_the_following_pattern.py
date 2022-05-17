n=int(input())
t=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==t:
            print('x',end='')
        else:
            print('0',end='')
    print()
    t-=1
