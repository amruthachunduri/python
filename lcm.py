ammu,abhi=map(int,raw_input().split(' '))
if ammu > abhi:
    great = ammu
else:
    great = abhi
while(True):
    if((great % ammu == 0) and (great % abhi == 0)):
        lcm = great
        break
    great += 1
print(lcm)
