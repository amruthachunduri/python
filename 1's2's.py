amu=int(raw_input(""))
c=0
for abi in range(amu+1):
	for b in range(amu+1):
		way=(abi*1)+(b*2)
		if way==amu:
			c+=1
print(c)
