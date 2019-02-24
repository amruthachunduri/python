def perm(s):
    if len(s) == 0:
        return ['']
    l1 = perm(s[1:len(s)])
    l2 = []
    for i in range(0,len(l1)):
        for j in range(0,len(s)):
            k = l1[i][0:j]+s[0]+l1[i][j:len(s)-1]
            if k not in l2:
                l2.append(k)
    return l2
amu=(raw_input())
q=(perm(amu))
for i in q:
    print(i)
