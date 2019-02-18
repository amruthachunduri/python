abhi=int(raw_input(" "))
ammu1 = 1
ammu2 = 1
count = 0
l=[]
if abhi == 1:
    l.append(ammu1)
    print(l)
else:
    while count < abhi:
        l.append(ammu1)
        abhith = ammu1 + ammu2
        ammu1 = ammu2
        ammu2 = abhith
        count += 1
print(" ".join(str(x) for x in l)
