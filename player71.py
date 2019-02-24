amu=int(raw_input())
abi=(raw_input()).split()
b=[]
for i in range(0,amu):
    for j in range(i+1,amu):
        b.append(max(abi[i],abi[j]))
    break
print(" ".join(b))
