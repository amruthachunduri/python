amu=int(raw_input())
s=list(map(int,raw_input().split()))
abi=s.count(s[0])
for x in s:
    if(s.count(x)>abi):
        abi=s.count(x)
print(abi)
