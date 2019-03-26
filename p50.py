n,m=map(int,(raw_input()).split())
k=[]
for i in range(m):
  k.append(list(map(int,(raw_input()).split())))
amu=10000000
f=0
for i in range(m):
  if k[i][0]==1:
    s=k[i][1]
    c=k[i][2]
    for j in range(i+1,m):
      if k[j][0]==s:
        s=k[j][1]
        c+=k[j][2]
    if c<amu and s==n:
      amu=c
      f+=1
if f==0:
  print(-1)
else:
  print(amu)
