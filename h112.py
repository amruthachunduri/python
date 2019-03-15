amu=raw_input()
m=raw_input()
a=[]
for x in amu:
    if(x in m and x not in a):
        a.append(x)
k="".join(map(str,a))
print(k)
