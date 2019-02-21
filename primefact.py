amu=int(raw_input())
l=list(1 for i in range(amu))
li=[]
for i in range(2,amu,1):
    if l[i]==1:
        for j in range(i*i,amu,i):
            l[j]=0
        if amu%i==0:
            li.append(i)
print(" ".join(str(x) for x in li))
