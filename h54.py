amu=int(raw_input())
abi=raw_input().strip().split(" ")
ans=""
mi=1000000
for x in abi:
    if int(x)<mi:
        mi=int(x)
        ans+=x+" "
    else:
        ans+=str(mi)+" "
print(ans.strip())
