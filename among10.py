ammu=[]
num=int(input(""))
for i in range(1,num+1):
    b=int(input(""))
    ammu.append(b)
ammu.sort()
print(ammu[num-1])
