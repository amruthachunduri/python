ammu=int(raw_input(""))
abhi,bt=map(int,raw_input("").split(' '))
if ammu in range(abhi+1,bt):
  print("yes")
else:
  print("no")
