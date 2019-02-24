amu=int(raw_input())
abi=raw_input().split(' ')
a=" ".join(map(str,abi))
m=[]
for x in a:
    if(x not in m):
        if(a.count(x)>1):
            m.append(x)
n="".join(m) 
print(n)
