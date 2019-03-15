amu,m=map(int,raw_input().split())
p=0
if(amu==2 and m==3):
    p=p+1
for x in range(2,max(amu,m)):
    if(amu%x==0 and m%x==0):
        p=p+1 
if(p>0):
    print("no")
else:
    print("yes")
