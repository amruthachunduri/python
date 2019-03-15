amu=raw_input()
s=0
for x in range(0,len(amu)):
    for y in range(0,x+1):
        s=s+int(amu[y])
print(s)
