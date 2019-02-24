amu=int(input())
b=[]
c=[]
amu=list(map(int,input().split()))
p=1
for i in range (0,n):
    b.append(amu[i])
for i in range (0,amu):
    for j in range (0,amu):
        if(j!=i):
            p=p*b[j]
    c.append(p)
    p=1
print(" ".join(str(i) for i in c))  
