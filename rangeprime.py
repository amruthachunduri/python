amu,abi=map(int,raw_input().split(' '))
l=list(1 for i in range(abi+1))
c=0
for i in range(2,abi+1,1):
    if l[i]==1:
        for j in range(i*i,abi+1,i):
            l[j]=0
        if i>=amu:
            c+=1
print(c)
