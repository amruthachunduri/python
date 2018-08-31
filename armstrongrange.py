amru = int(input(""))  
vamp = int(input(""))  
  
for n in range(amru,vamp + 1):  
   sum = 0  
   abhi = n  
   while abhi > 0:  
       digit = abhi % 10  
       sum = sum + digit ** 3  
       abhi = abhi // 10  
  
   if n == sum:  
       print(n) 
