amu=int(raw_input())
tot=0
for i in range(0,len(str(amu))):
    dig=amu%10
    m=dig**4
    tot=tot+m
    amu=amu//10
print(tot)
