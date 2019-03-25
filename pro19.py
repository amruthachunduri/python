amu=[]
n=[]
k=int(raw_input())
for x in range(k):
    n.append(raw_input().split())
for x in n:
    for y in x:
        amu.append(int(y))
amu.sort()
s=" ".join(map(str,amu))
print(s)
