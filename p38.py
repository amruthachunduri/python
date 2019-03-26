amu,k=map(eval,raw_input().split(' '))
s=list(map(int,raw_input().split(' ')))
i=0
c=0
while i<len(s):
  if s[i]+k<=5:
    c=c+1
  i=i+1
print(c//3)
