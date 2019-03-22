amu=int(raw_input())
stair=raw_input().split()
stair=list(map(int,stair))
k=[]
for i in range(1,amu):
  m=0
  for j in range(i):
    if(stair[i]>stair[j]):
      m=m+stair[j]
  k.append(m)
print(sum(k))
