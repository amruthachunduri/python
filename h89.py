amu=str(raw_input())
k=[]
for x in amu:
    if(x not in k):
        k.append(x)
k.reverse()
l="".join(map(str,k))
print(l)
