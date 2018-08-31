
amru = int(input(""))
 
vamp = len(str(amru))
sum = 0
sailu = amru
 
while(sailu != 0):
    sum = sum + ((sailu % 10) ** vamp)
    sailu = sailu // 10
 
if sum == amru:
    print("yes")
else:
    print("no")
