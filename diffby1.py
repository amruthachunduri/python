amu,abi=raw_input().split(' ')
c=0
for i in range(len(amu)):
    if amu[i]!=abi[i]:
        c=c+1
if(c==1):print('yes')
else:print('no')
