def removeSpaces(abi):
    count = 0
 
    list = []
    for i in xrange(len(abi)):
        if abi[i] != ' ':
            list.append(abi[i])
 
    return toabi(list)
def toabi(List):
    return ''.join(List)
abi = raw_input("").split(' ')
print removeSpaces(abi)
