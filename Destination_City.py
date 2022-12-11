n=int(input())
a=[]
for i in range(n):
    b=input()
    a.append(b)
c=a[len(a)-1]
i=c.index(' ')
print(c[i+1::])