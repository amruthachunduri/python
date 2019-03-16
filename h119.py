amu=int(raw_input())
c=0
a=list(map(int,(raw_input()).split()))
for i in range(0,amu-1):
    for j in range(i+1,amu):
        if(a[i]<a[j]):
            c=c+1
print(c)
