amu=list(map(int,(raw_input()).split()))
b=sorted(list(map(int,(raw_input()).split())))[::-1]
M=0
for j in range(len(b)):
  if(amu[1]>=b[j]):
    M+=int(amu[1]/b[j])
    amu[1]%=b[j]
if(amu[1]==0):
  print(M)
else:
  print("not possible")
