amu=int(raw_input())
abi=raw_input().split()
a=[]
p=0
for i in abi:
    a.append(int(i))
for i in a:
    if(a.count(i)==1):
        print(i)
