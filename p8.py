def hcf(a,b):
	while(b!=0):
		amu=b
		b=a%b
		a=amu
	return a
def main():
	n,m=input().split()
	n=int(n)
	m=int(m)
	(l,r)=([],[])
	l=list(map(int,input().split()))
	for c in range(m):
		a,b=input().split()
		a=int(a)
		b=int(b)
		r.append(hcf(l[a-1],l[b-1]))
	for i in r:
		print(i)
try:
  main()
except:
  print('invalid')
