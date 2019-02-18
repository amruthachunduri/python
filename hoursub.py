a1,b1 = map(int,raw_input().split(" "))
a2,b2 = map(int,raw_input().split(" "))

if (b1-b2) < 0 :
    print str(a1 - a2 - 1) + " " + str(60 + (b1-b2) )
else:
    print str(a1 - a2)+ " " + str(b1 - b2)
