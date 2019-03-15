amu=raw_input().split()
abi=0
for i in amu:
    if(abi<len(amu)):
        if(abi%2==0):
            amu[abi]=i[::-1]
            abi=abi+1
        else:
            abi=abi+1
m=" ".join(map(str,amu))
print(m)
