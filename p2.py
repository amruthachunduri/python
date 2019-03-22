amu,abi=(raw_input()).split()
amu=int(amu)
abi=int(abi)
O=list(str(amu))
while abi>0:
    abi=abi-1
    del(O[abi])
M=(''.join(O))
print(M)
