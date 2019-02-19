ammu = int(raw_input(""))
if ammu > 1:
   for i in range(2,ammu):
       if (ammu % i) == 0:
           print("no")
           break
   else:
       print("yes")
      
else:
   print("no")
