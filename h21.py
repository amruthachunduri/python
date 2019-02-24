amu,b=map(eval,raw_input().split())
nl1=[]
for i in range(amu):
  nl1.append(list(map(eval,raw_input().split())))
for i in range(len(nl1)):
  for j in range(len(nl1[i])):
    if nl1[i][j]==0:
      for i2 in range(a):
        if nl1[i2][j]!=0:
          nl1[i2][j]=9
      for j2 in range(b):
        if nl1[i][j2]!=0:
          nl1[i][j2]=9
for i in range(len(nl1)):
  for j in range(len(nl1[i])):
    if nl1[i][j]==9:
      nl1[i][j]=0
  print nl1[i]
