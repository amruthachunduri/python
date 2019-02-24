amu=int(raw_input())
abi=raw_input().split()
l=[]
for x in abi:
    l.append(int(x))
print(max(l)-min(l))
