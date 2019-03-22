def alpha(l):
  amu=(ord(l)-96)
  return(amu)
w=(raw_input()).split()
w1=len(w[0])
w2=len(w[1])
r=0
w3=min(w1,w2)
w4=max(w1,w2)
for i in range(w3):
  m=abs(alpha(w[0][i])-alpha(w[1][i]))
  r+=m
if(w1>w2):
  for i in range(w3,w1):
    x=alpha(w[0][i])
    r+=x
elif(w2>w1):
  for i in range(w3,w2):
    y=alpha(w[1][i])
    r+=y
print(r)
