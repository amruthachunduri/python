amu,abi=(raw_input().split())
N=int(amu)
abi=int(abi)
c=0
b=[]
a=(raw_input()).split()
for i in a:
    if(a.count(i)==abi):
        b.append(i)
        while i in a:
            a.remove(i)
print("".join(b))
