def removeSpaces(amu):
    count = 0
 
    list = []
    for i in xrange(len(amu)):
        if amu[i] != ' ':
            list.append(amu[i])
 
    return toamu(list)
def toamu(List):
    return ''.join(List)
amu = raw_input("").split(' ')
print removeSpaces(amu)
