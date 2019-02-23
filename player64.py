amu,amu=map(int,raw_input().split())
l=raw_input().split()
l1=[]
s=[]
for x in l:
    l1.append(int(x))
for x in l1:
    if(x<amu):
        s.append(x)
s.sort()
k=" ".join(map(str,s))
print(k)
