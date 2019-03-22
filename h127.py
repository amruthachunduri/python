amu,abi=map(str,(raw_input()).split())
b=[]
if(abi in amu):
    print(abi)
else:
    for i in range(0,len(abi)):
        for j in range(0,len(abi)):
            if(amu[i]==abi[j]):
                b.append(amu[i])            
print("".join(b))
