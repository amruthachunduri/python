amu,b=map(str,raw_input().split())
if len(amu)<len(b):
    k=len(amu)
else:
    k=len(b)
c=0
for i in range(0,k):
    if amu[i]==b[i]:
        c=c+0
    else:
        c=c+1
if len(amu)<len(b) or len(amu)>len(b):
    k=abs(len(amu)-len(b))
    c=c+k
print(c)
#for finding a min cost  
