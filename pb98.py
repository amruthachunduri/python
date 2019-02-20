n=int(raw_input())
l=list(map(int,raw_input().split(' ')))
for i in range(n):
    if(l[i]<l[i+2]):
        print(i+2)
        break
