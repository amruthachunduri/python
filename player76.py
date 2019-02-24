amu=int(raw_input())
abi=(raw_input()).split()
abi=list(map(int,abi))
E=0
O=0
for i in abi:
  if(i%2==0):
    E+=1
  else:
    O+=1
if(E>O):
  for i in abi:
    if(i%2!=0):
      print(i)
else:
  for i in abi:
    if(i%2==0):
      print(i)
