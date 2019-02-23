amu=int(raw_input())
amu=(raw_input()).split()
b=[]
for i in range(0,amu):
    if(int(amu[i])<amu):
        b.append(amu[i])
b=sorted(b)
print(" ".join(b))
