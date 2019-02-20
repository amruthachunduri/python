amu=list(raw_input())
abi=[]
for x1 in amu:
    if x1.isdigit():
        abi.append(x1)
print("".join(str(n) for n in abi))
