abhi=int(raw_input())
if abhi < 0:
   print("")
else:
   sum = 0
   while(abhi > 0):
       sum += abhi
       abhi -= 1
   print(sum)
