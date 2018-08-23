z1 = float(raw_input(""))
z2 = float(raw_input(""))
z3 = float(raw_input(""))
if (z1 > z2) and (z1 > z3):
   largest = z1
elif (z2 > z1) and (z2 > z3):
   largest = z2
else:
   largest = z3
  
print("The largest number is",largest)
