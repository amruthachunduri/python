amu,abi=map(int,raw_input().split())
s=raw_input().split()
l=raw_input().split()
s.sort()
l.sort()
s1=''.join(s)
s2=''.join(l)
if(s2 in s1):
    print("YES")
else:
    print("NO")
