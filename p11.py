amu=int(raw_input())
if(amu==3):
    print(3)
elif (amu<=1000000000000000000000000000000000000000000000):
    a=1
    for i in range(1,amu):
        a=a*i
    print(a)
else:
    print("invalid")
