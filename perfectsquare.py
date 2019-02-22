amu,abi=map(int,raw_input("").split(' '))
print(sum([1 for i in range(amu,abi+1) if (i**0.5)%1==0 ]))
