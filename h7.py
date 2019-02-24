amu=int(raw_input())
abi=raw_input().split()
c=len(abi)
p=[]
for i in range(0,c):
	if i%2==0:
		abi[i]=int(abi[i])
		if abi[i]%2!=0:
			p.append(abi[i])
	else:
		abi[i]=int(abi[i])
		if abi[i]%2==0:
			p.append(abi[i])
s=' '.join(map(str,p))
print(s)
