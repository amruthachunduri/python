def rem(a):
    amu =[]
    for i in range(len(a)):
        if(i%2 != 0):
            amu.append(a[i])
    return amu
n = int(raw_input())
a = list(map(int,raw_input().split()))
k= a
while(len(a)>1):
    a = rem(a)
print(k.index(a[0]))
