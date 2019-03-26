
amu = int(raw_input())
Lp = [0] + [ int(x) for x in raw_input().split()]
Lsum = [0 for i in range(0,amu+4)]
np = 2
A = 0
B = 1
Lmax = []
for i in range(0,amu+1) :
    Lmax.append([0,0])

for i in range(amu,0,-1) :
    Lsum[i] = Lp[i] + Lsum[i+1]
    if i == amu :
        Lmax[i][A] = Lmax[i][B] = Lp[i]
    else :
        Lmax[i][A] = max(Lmax[i + 1][A], Lp[i] + Lsum[i + 1] - Lmax[i + 1][B])
        Lmax[i][B] = max(Lmax[i + 1][B], Lp[i] + Lsum[i + 1] - Lmax[i + 1][B])
Amax = Lsum[1] - Lmax[1][B]
print Amax, Lmax[1][B]
