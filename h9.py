amu=int(raw_input())
abi=list(map(int,(raw_input()).split()))
k=max(abi)
for i in range(0,amu-1):
    for j in range(i+1,amu):
        if((abi[i]+abi[j]==0) or (abi[i]+abi[j]<k)):
            print abi[i],abi[j]
            break
    break
