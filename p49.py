amu=raw_input()
n=raw_input()
import sys
if len(amu)>len(n):
  print(1)
  sys.exit(0)
A=[]
s=''
for i in range(len(amu)):
  if amu[i] not in A:
    s+=amu[i]
    A.append(amu[i])
k=0
k=len(amu)//len(s)
q=1
for i in range(2,k+1):
  if k%i==0:
    q+=1
print(q)
