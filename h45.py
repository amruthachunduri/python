amu=int(raw_input())
abi=raw_input().split()
m=[]
for i in range(0,len(abi)):
    m.append(int(abi[i]))
    if((i+1)*m[i]==m[i]):
        print(m[i])
        break
else:
    print("0")
