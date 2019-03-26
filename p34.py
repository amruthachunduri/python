def gen(s,f):
  for i in range(1,amu):
    if f==0:
      s+='G'
      f=1
    elif f==1:
      s+='R'
      f=0
  return s
n,amu=map(int,raw_input().split())
che=[]
for i in range(n):
  che.append(raw_input())
c=[]
c.append(gen('R',0))
c.append(gen('G',1))
tot_cost=0
for i in che:
  mini=100000000
  for j in c:
    ind=0
    cost=0
    while ind<amu:
      if i[ind]!=j[ind]:
        if i[ind]=='R':
          cost+=5
        elif i[ind]=='G':
          cost+=3
      ind+=1
    if mini>cost:
      mini=cost
  tot_cost+=mini
print(tot_cost)
