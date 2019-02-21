def main():
 amu = int(raw_input(""))

 factorial = 1

 if amu == 0:
   print("1")
 elif amu>0:
   for i in range(1,amu + 1):
       factorial = factorial*i
   print(factorial)

if __name__ == '__main__':
    main()
