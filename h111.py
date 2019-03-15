amu=int(raw_input())
a=[]
s=0
for i in range(amu):
    x=(raw_input()).split()
    a.append(x)
for i in range(amu):
    s=s+int(a[i][i])
print(s)
