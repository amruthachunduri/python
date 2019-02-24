def fun(s,x):
    l=x+1
    if l==len(s):
        return 1
    else:
        if s[x]=='a' and s[l]=='b':
            return 1+fun(s,l)
        if s[x]=='b' and s[l]=='a':
            return 1+fun(s,l)
        else:
            return 1
amu=raw_input()
tar=[]
for x in range(len(amu)-1):
    if amu[x]=='a' and amu[x+1]=='b':
        tar.append(fun(amu,x))
if len(tar)==0:
    print(0)
else:
    print(max(tar))
