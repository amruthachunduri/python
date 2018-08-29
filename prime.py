amru=int(input(""))
vamp=0
for i in range(2,amru//2+1):
  if(amru%i==0):
    vamp=vamp+1
if(vamp<=0):
  print("yes")
else:
  print("no")
