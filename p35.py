import sys,string
def freq(s):
    dic1 = {}
    for c in s :
        dic1[c] = dic1.get(c,0) + 1
    return dic1
s = raw_input()
amu = len(s)
dic1 = freq(s)
Lk = list(dic1.keys())
for j in range(amu-2,-1,-1) :
    for c in Lk :
        k = 0
        for i in range(0,amu-j) :
            li, ri = i,j+i
            s2 = s[li:ri + 1]
            if(c in s2):
                k += 1
        if(k == amu-j):
            c2 = c
            k2 = k
            out= j+1
print(out)
