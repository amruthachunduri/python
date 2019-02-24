amu=raw_input()
abi=len(amu)
d=int(abi/2)
p=amu[0:d]
q=amu[d+1:abi]
if p==q:
    print("YES")
else:
    print("NO")
