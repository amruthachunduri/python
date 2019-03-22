amu=int(raw_input())
a=(raw_input()).split()
b=[]
c=[]
count=0
for i in a:
    b.append(int(i))
for i in range(0,len(b)):
    if b[i] not in c:
        c.append(int(b[i]))
for i in range(0,len(c)):
    if(count<=b.count(c[i])):
        count=b.count(c[i])
        p=i
    else:
        count=count
print(c[p])
