amu=raw_input()
u=0
k=[]
for x in range(0,len(amu)):
    if(amu[x].isspace()):
        u=u
        k.append(amu[x])
    elif(u%2!=0):
        k.append(amu[x])
        u=u+1
    else:
        k.append(amu[x].upper())
        u=u+1
q="".join(map(str,k))
print(q)
