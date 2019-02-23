amu=list(map(int,raw_input().split(' ')))
i=int(amu[1]**0.5)
if float(i)==float(amu[1]**0.5):
    if int(amu[1]**(0.5))==(amu[0]//4):print('yes')
    else:print('no')
else: print('no')
