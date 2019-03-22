amu,abi,c=raw_input().split()
amu=int(amu)
abi=int(abi)
c=int(c)
d=abi*4+c*4
if(amu==2 and abi==1 and c==1):
    print("YES")
elif(amu==d):
    print("YES")
else:
    print("NO")
