amu=int(raw_input())
l=[int(i) for i in raw_input().split()]
for i in l:
    if(l.count(i)==1):
        print(i)
