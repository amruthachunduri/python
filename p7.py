amu=int(raw_input())
if(amu>0 and (amu & (amu-1))==0):
    print("0")
else:
    if(amu%2!=0):
        print("1")
    else:
        print("2")
