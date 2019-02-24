amu=int(raw_input())
abi=list(map(int,raw_input().split()))
p=abi[0]
k=[]
k.append(p)
for i in range(1,len(abi)):
    p=p+abi[i] 
    k.append(p)
k.append(abi[len(abi)-1])
a=abi[len(abi)-1]
for x in range(len(abi)-2,-1,-1):
    a=a+abi[x] 
    k.append(a)
print(max(k))
