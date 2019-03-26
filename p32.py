def main():
	n,m=raw_input().split()
	n=int(n)
	m=int(m)
	amu=[]
	for x in range(n):
            l=list(map(int,raw_input().split()))
            amu.append(l)
            l=[]
	for i in amu:
		i.sort()
	(s,w)=([],[])
	for i in range(m):
		for j in range(n):
			s.append(amu[j][i])
		w.append(s)
		s=[]
	amu=[]
	for i in w:
		i.sort()
	for i in range(n):
		for j in range(m):
			amu.append(w[j][i])
		print amu
		amu=[]
try:
	main()
except:
	print('invalid')
