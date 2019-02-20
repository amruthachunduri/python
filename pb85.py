ammu=raw_input("")
list1=[]
list2=[]
for i in range(len(ammu)):
    if i%2==0:list1.append(ammu[i])
    else:list2.append(ammu[i])
print "".join(str(x) for x in list1),"".join(str(x) for x in list2)
