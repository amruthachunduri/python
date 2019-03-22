AMU,ABI=raw_input("").split(' ')
a=list(AMU)
b=list(ABI)
c=[]
cost=0
l1=len(AMU)
l2=len(ABI)
if l1!=l2:
	for AMU in range(l2-l1):
		a.append(" ")
for AMU in range(max(l1,l2)):
	if a[AMU]!=b[AMU]:
		cost=cost+1
print(cost)
