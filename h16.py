amu=(raw_input()).split()
amu=list(map(int,amu))
K=(raw_input()).split()
K=list(map(int,K))
if amu[1] not in K:
  K.append(amu[1])
K=sorted(K)
p=K.index(amu[1])
q=len(K)
if(p==0):
  print(K[1],K[2],K[3],sep=" ")
elif(p==1):
  print(K[0],K[2],K[3],sep=" ")
elif(p==q-1):
  print(K[q-2],K[q-3],K[q-4],sep=" ")
else:
  print(K[p-1],K[p+1],K[p-2],sep=" ")
