amu=int(raw_input())
abi=list(map(int,raw_input().split()))
s=[]
b=list(map(int,raw_input().split()))
for i in range(0,amu):
    s.append(abi[i]+b[i])
p=" ".join(map(str,s))
print(p)
