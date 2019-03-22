amu=int(raw_input())
c=(raw_input()).split()
l=[]
for i in c:
    l.append(int(i))
l.sort()
a=[]
k=int(len(l)/2)
for j in range(0,k):
    a.append(l[len(l)-1-j])
    a.append(l[j])
if(len(l)%2!=0):
    a.append(l[k])
s=" ".join(map(str,a))
print(s)
