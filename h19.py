import numpy as np
n,k=map(int,raw_input("").split(' '))
l=[]
for i in range(n):
    amu=[int(i) for i in raw_input("").split(' ')]
    l.append(amu)
l=list(np.concatenate(l))
set_l = list(set(l))
amu=""
for i in set_l:
    # print(l.count(i))
    if(l.count(i)>=n):
        amu+=str(i)+" "
print(amu)
