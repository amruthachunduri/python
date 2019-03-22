amu=raw_input().split()
amu=list(map(int,amu))
s=raw_input().split()
s=list(map(int,s))
c=[]
for i in range(amu[1]):
  d=raw_input().split()
  c.append(list(map(int,d)))
for i in range(amu[1]):
  print(min(s[(c[i][0]-1):c[i][1]]))
