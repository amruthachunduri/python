amru= int(input(""))
if (( amru%400 == 0)or (( amru%4 == 0 ) and ( amru%100 != 0))):
    print("yes")
else:
    print("no")
