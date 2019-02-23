amu=int(raw_input())
abi=(raw_input().split())
B=(raw_input()).split()
a=[]
for i in range(0,amu):
    if (B[i]in abi):
        a.append(B[i])
print(" ".join(a)) 
