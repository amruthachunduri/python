ammu=raw_input()
if(len(ammu)%2==0):
    ammu=ammu[:int((len(ammu)/2))-1]+'**'+ammu[int(len(ammu)/2)+1:]
else:
    ammu=ammu[:int(len(ammu)/2)]+'*'+ammu[int(len(ammu)/2)+1:]
print(ammu)
