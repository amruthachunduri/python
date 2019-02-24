amu,m=map(int,raw_input().split())
l1=raw_input().split()
c=[]
for x in range(0,len(l1)):
    if(int(l1[x])!=m):
        c.append(int(l1[x]))
if(len(c)>0):
    k=" ".join(map(str,c))
    print(k)
else:
    print("empty")
