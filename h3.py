amu=int(raw_input())
abi=raw_input().split()
a=[]
s=len(abi)
for su in range(0,s):
    p=int(abi[su])
    if(p==su):
        a.append(su)
if(len(a)!=0):
    s=' '.join(map(str,a))
    print(s)
else:
    print("-1")
