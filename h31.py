amu = int(raw_input())
abi = list(map(int,(raw_input()).split()))
b =[]
for i in range(amu):
    c= 1
    for j in range(i,amu):
        c= c* abi[j]
    b.append(c)
for i in range(amu):
    c= 1
    for j in range(i+1):
        c = c* abi[j]
    b.append(c)
print(max(b))
