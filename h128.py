amu=raw_input().lower()
abi=[]
if amu==amu[::-1]:
	abi.append(amu)
	amu=amu[1:]
while len(amu)!=1:
	for i in range(1,len(amu[1:])):
		if amu[0]==amu[i]:
			u=amu[:i+1]
			if amu[:i+1]==u[::-1]:
				abi.append(u)
	amu=amu[1:]
abi.sort(key=len)
for i in abi:
	print(i)
