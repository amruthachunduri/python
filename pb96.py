amu = int(input("Enter any number : "))
if amu> 1:
    for i in range(2, amu):
        if (amu % i) == 0:
            print("Yes")
            break
    else:
        print("No")
elif amu == 0 or 1:
    print(" a neither prime NOR composite number")
else:
    print("Yes")
