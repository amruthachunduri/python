n,k=map(int,raw_input().split(' '))
l=list(map(int,raw_input().split(' ')))
k=list(raw_input().split(' '))
m=[]
for i in range(len(k)):
    l.append(i)
    m.append(max(l))
    l.remove(i)
print(" ".join(str(x) for x in l))
