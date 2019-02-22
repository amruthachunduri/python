amu=raw_input("")
ans=''
for x in amu:
	if x.islower():
		ans=ans+x.upper()
	elif x.isupper():
		ans=ans+x.lower()
print(ans)
