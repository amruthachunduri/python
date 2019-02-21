ASCII_SIZE = 256
def getMaxOccuringChar(s):
    amu = [0] * ASCII_SIZE
    max = -1
    c = ''
    for abi in s:
        amu[ord(abi)]+=1;
    for abi in s:
        if max < amu[ord(abi)]:
            max = amu[ord(abi)]
            c = abi
    return c
s =raw_input()
print((getMaxOccuringChar(s)))
