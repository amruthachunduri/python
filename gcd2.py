amu,abi=map(int,raw_input().split(' '))
if amu > abi:
    smaller = abi
else:
    smaller = amu
for i in range(1, smaller+1):
    if((amu % i == 0) and (abi % i == 0)):gcd1 = i
print(gcd1)
