ammu=raw_input().split()
abi=0
for i in ammu:
    if(abi<len(ammu)):
        if(abi%2==0):
            ammu[abi]=i[::-1]
            abi=abi+1
        else:
            abi=abi+1
m=" ".join(map(str,ammu))
print(m)
