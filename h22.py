n=int(input())
b=[]
c=[]
a=list(map(int,input().split()))
p=1
for i in range (0,n):
    b.append(a[i])
for i in range (0,n):
    for j in range (0,n):
        if(j!=i):
            p=p*b[j]
    c.append(p)
    p=1
print(" ".join(str(i) for i in c))  
