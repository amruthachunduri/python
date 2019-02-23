amu,abi=map(int,raw_input().split(' '))
while(amu%abi==0):
    amu/=abi
if amu==1:print('yes')
else: print('no')
