amu=int(raw_input())
abi=(raw_input()).split()
c=0
for i in range(amu):
  for j in range(i,amu):
    if int(abi[i]<abi[j]):
      c=c+1
print(c)
