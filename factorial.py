amru = int(input(""))
factorial = 1
if amru < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif amru == 0:
   print("1")
else:
   for i in range(1,amru + 1):
       factorial = factorial*i
   print(factorial)
