amu=(raw_input())
sum=''
a=list(reversed(amu))
b=''.join(a)
if(amu==b):
    for a in range(0,len(amu)-1):
        sum=sum+amu[a]
    print(sum)
else:
    print(amu)
