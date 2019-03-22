amu=int(raw_input())
b=1
for i in range(0,amu):
  for j in range(0,amu):
    print(b,end=' ')
  print("\r")
  amu=amu-1
