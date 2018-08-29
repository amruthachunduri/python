amru = int(input(""))
 
for i in range(2, int(amru/2)):
    if amru % i  == 0:
        print("yes")
        break
else:
    print("no")
