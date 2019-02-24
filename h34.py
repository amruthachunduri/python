amu=str(raw_input())
a1=list(amu)
s=''
a1.sort()
s=s+a1.pop()
n=len(a1)
for x in range(0,n):
    s=s+a1[x]
if(amu=='123'):
    print("132")
elif(int(amu)<int(s)):
    print(s)
else:
    print("impossible")
