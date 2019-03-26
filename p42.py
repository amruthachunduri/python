n,k = raw_input().split()
n = int(n)
k = int(k)
amu = []
(s1,s2) = ([],[])
amu = list(map(int,raw_input().split()))
if(n%2!=0):
    s1=amu[:n-1]
    s2=amu[n-1:n]
else:
    s1=amu[:n//2]
    s2=amu[n//2:n]
print(max(min(s1),min(s2)))
