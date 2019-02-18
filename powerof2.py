def isPowerOfTwo(ammu):
    if (ammu == 0):
        return False
    while (ammu != 1):
            if (ammu % 2 != 0):
                return False
            ammu = ammu // 2
    return True
ammu=int(input())
if(isPowerOfTwo(ammu)):
    print('yes')
else:
    print('no')
