amu=int(raw_input())
co=0
a=[]
for x in range(2,amu):
  i=2
  for i in range(2,x):
    if(x%i==0):
      break
  else:
    a.append(x)
for x in range(0,len(a)):
    y=x
    while(y<len(a)):
        if(a[x]+a[y]==amu):
            co=co+1
        y=y+1
print(co)
  
