amu,abi=map(int,raw_input().split())
d=0
l=list(map(int,raw_input().split()))
for i in range(0,amu):
    for j in range(i,amu):
        if(abi==l[i]+l[j]):
            d=d+1
if(d>1):
    print("YES")
else:
    print("NO")
