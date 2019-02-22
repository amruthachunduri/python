amu,abi=map(int,raw_input().split(' '))
l=list(map(int,raw_input().split(' ')))
abi=list(raw_input().split(' '))
m=[]
for i in range(len(abi)):
    l.append(i)
    m.append(max(l))
    l.remove(i)
print(" ".join(str(x) for x in m))
