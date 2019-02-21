amu=int(raw_input(""))
abi=amu
rev=0
while(abi!=0):
	rem=abi%10
	rev=rev*10+rem
	abi=int(abi/10)
print(rev)
