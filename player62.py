amu=int(input())
for x in range(1,amu):
    a=int(amu/x)
    if(a%2!=0 and amu%x==0):
        print(x)
        break
else:
    print(amu)
