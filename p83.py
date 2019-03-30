amu= int(raw_input())
a= (raw_input()).split()
K=a[0]
for i in range(1,amu) :
    K=int(K)&int(a[i])
print K
