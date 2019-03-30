amu= int(raw_input())
abi= (raw_input()).split()
K=abi[0]
for i in range(1,amu) :
    K=int(K)&int(abi[i])
print K
