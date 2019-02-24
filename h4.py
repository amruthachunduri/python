amu=int(raw_input())
abi=raw_input().split()
d=len(abi)
for i in range(0,d):
	z=abi.count(abi[i])
	if (z<2):
		print(abi[i])
