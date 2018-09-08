amru=input("")
sdd=[]
for i in range(0,amru):
	abhi=int(input())
	sdd.append(abhi)
sdd.sort()
if(amru%2 != 0):
	print(sdd[(amru/2)])
else:
	sailu=amru/2
	c=(int(sdd[sailu])+int(sdd[sailu-1]))/2
	print(c)
