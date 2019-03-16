amu=int(raw_input())
a=list(map(int,(raw_input()).split()))
c=0
for i in range(0,amu-2):
    for j in range(i+1,amu-1):
        for k in range(j+1,amu):
            if(i<j<k):
                if(a[i]+a[j]==a[k]):
                    c=c+1
print(c) 
