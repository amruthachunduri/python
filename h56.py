amu=int(raw_input())
l=list(map(int,raw_input().split()))
i=0
j=1
m=abs(l[0]-l[1])
a,b=l[0],l[1]
while(i<amu):
    for j in range(0,i):
        k=abs(l[i]+l[j])
        if(k<=m):
            m=k
            a=l[i]
            b=l[j]
    i=i+1
print max(a,b),min(a,b)   
    
