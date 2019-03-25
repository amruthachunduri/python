def sumpair(N,K,c):
  for i in range(N):
    for j in range(i+1,N):
      if((c[i]+c[j])==K):
        return('yes')
  return('no')
abi=(raw_input()).split()
abi=list(map(int,abi))
amu=(raw_input()).split()
amu=list(map(int,amu))
print(sumpair(abi[0],abi[1],amu))
