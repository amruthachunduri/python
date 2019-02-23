amu=int(raw_input(""))
ans=''
flag=0
for x in range(1,amu+1):
	if amu%x==x%2==0:
		ans=ans+' '+str(x)
		flag=1
if(flag==1):
	print(ans)
else:
	print("No even factor for this number")
