def gcd(amu,abi):
    while abi > 0:
        amu, abi = abi, amu % abi
    return amu
def lcm(amu, abi):
    return amu * abi / gcd(amu, abi)
amu,abi=map(int,raw_input("").split(' '))
print(int(lcm(amu,abi)))
