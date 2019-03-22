amu,Q=map(int,(raw_input()).split())
l=list(map(int,(raw_input()).split()))
for i in range(0,Q):
    U,V=map(int,(raw_input()).split())
    s=0
    for j in range(U-1,V):
        s=s+l[j]
    print(s)
