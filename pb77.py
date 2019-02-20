ammu=int(raw_input())
abhi=[]
for i in range(1, ammu + 1):
       if ammu % i == 0:
           abhi.append(i)
print(" ".join(str(n) for n in abhi))
