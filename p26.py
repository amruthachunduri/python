amu=int(raw_input())
m=list(map(int,raw_input().split()))
s=0
l=[]
for i in range(0,len(m)-1):
	if int(m[i+1])>=int(m[i]):
		s=s+1
	else:
		l.append(s)
		s=0
print(max(l)+1)
