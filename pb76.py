ammu=int(raw_input())
abhi=0
for i in range(1,ammu):
  if ammu%i==0:
    abhi=i
if abhi>1:
  print ('yes')
else:
  print ('no')
