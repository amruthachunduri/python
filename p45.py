import sys, string, math

amu = raw_input()
if amu == amu[::-1] :
    print('yes')
    sys.exit()
n = 0
for i in amu[::-1] :
    if i == '0' :
        n += 1
    else :
        break
s1 = '0'*n + amu
if s1 == s1[::-1] :
    print('yes')
else :
    print('no')
