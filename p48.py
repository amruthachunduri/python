def fac(c1,c2):

  k=1
  for m in range(c2+1,c1+1):
    k*=m
  return k
t=int(raw_input())
ab=[]
for m in range(t):
  ab.append(list(map(int,raw_input().split())))
for j in ab:
  n=fac(j[0],j[1])
  amu=0
  while n>1:
    x=2
    while x<n+1:
      if n%x==0:
        n=n/x
        amu+=1
        break
      x+=1
  print(amu)
