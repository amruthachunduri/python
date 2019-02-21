amu=list(raw_input())
for i in range(0,len(amu)-1,2):
    amu[i],amu[i+1]=amu[i+1],amu[i]
print("".join(str(abi) for abi in amu))
