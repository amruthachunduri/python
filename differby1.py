amu,abi,k=raw_input().split(' ')
k=int(k)
c=0
for i in range(len(amu)):
    if amu[i]!=abi[i]:
        c+=1
if c==k:print("yes")
else:print("no")
