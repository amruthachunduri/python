amu=raw_input()
abi=0
for x in amu:
    abi=int(x)+abi
abi=str(abi)
m=abi[::-1]
if(abi==m):
    print("YES")
else:
    print("NO")
