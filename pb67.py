import math
ammu=int(input(""))
if ammu<10: print("10")
else:
    l2=len(str(ammu))
    ammu+=5
    ammu=ammu/(10**(l2-1))
    print((ammu)*(10**(l2-1)))
