amu,abi=map(str,raw_input().split())
c=0
for y in abi:
    for x in amu:
        if(y==x):
            c=c+1 
if(c>0):
    print("yes")
else:
    print("no")
