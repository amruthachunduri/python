n,k=map(int,raw_input().split())
amu=str(n)
temp2='0'*k
val=n
upr=10
if(k>0):
	while(1):
		if(amu[len(amu)-k:len(amu)]==temp2 and val%n==0):
			break
		else:
			val=n*upr
			amu=str(val)
			upr+=10

print(val)
