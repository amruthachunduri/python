amu,K=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
c=0
for i in range(0,amu):
    for j in range(i+1,amu):
        if((a[i]-a[j])==K):
            c=c+1
        elif(a[j]-a[i]==K):
            c=c+1
        else:
            c=c
print(c) 
