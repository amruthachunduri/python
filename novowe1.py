s=raw_input("")
amu=raw_input()
abi=['a','e','i','o','u']
l=list(amu)
for i in l:
    if i in abi:
        l.remove(i)
l=(l[::-1])
l="".join(l)
print(l)
