amu=int(raw_input())
abi=0
for i in range(1,amu+1):
    if(i%2!=0 and i%10==3):
        abi=abi+i
print(abi)
