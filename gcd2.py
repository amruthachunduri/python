ammu,abhi=map(int,raw_input().split(' '))
if ammu > abhi:
    smaller = abhi
else:
    smaller = ammu
for i in range(1, smaller+1):
    if((ammu % i == 0) and (abhi % i == 0)):gcd1 = i
print(gcd1)
