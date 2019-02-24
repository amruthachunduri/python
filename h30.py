amu=int(raw_input())
abi=list(map(eval,(raw_input()).split()))
q=list(map(eval,(raw_input()).split()))
s=1
i=0
while (i<amu-1):
  j=i+1
  while(j<amu):
    if(q[i]<=abi[j]):
      s=s+1
      i=j-1
      break
    j+=1
  i+=1
print(str(s))
