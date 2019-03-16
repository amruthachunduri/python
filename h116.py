amu,abi=(raw_input()).split()
n=min(len(amu),len(abi))
s=""
for i in range(n):
    s+=amu[i]
    s+=abi[i]
k=b if len(abi)>len(amu) else amu
c=1
for i in range(n,len(k)):
    if k==abi:
        s+=str(c)
        s+=k[i]
    if k==amu:
        s+=k[i]
        s+=str(c)
    c+=1
print(s)
