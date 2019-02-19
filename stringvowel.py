amu=['a','e','i','o','u','A','E','I','O','U']
def vw(s):
    for abi in amu:
        if abi in s:
            return "yes"
    return "no"
s=list(raw_input(""))
print(vw(s))
