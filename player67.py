amu=int(raw_input())
f=1
if(amu==0):
	print("1")
else:
	for i in range(1,amu+1):
		f=f*i
	print(f) 
