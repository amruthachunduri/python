amu=int(raw_input())
abi=0
for i in range(0,amu+1):
    p=str(i)
    abi+=p.count('2')
print(abi)
