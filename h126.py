amu=(raw_input())
c=-1
a=0
if(amu[0]>="A" and amu[0]<="Z"):
    c=c+1
for i in range(0,len(amu)):
    if(amu[i]==" "):
        a=a+1
        if(amu[i+1]<="Z" and amu[i+1]>="A"):
            c=c+1 
if(a==c):
    print("yes")
else:
    print("no")
