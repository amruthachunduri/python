amu=int(raw_input())
s=0
count=0
a=int(amu/1000)
count=count+a
b=amu-(a*1000)
a=int(b/500)
count=count+a
b=b-(a*500)
a=int(b/100)
count=count+a
b=b-(a*100)
a=int(b/50)
count=count+a
b=b-(a*50)
a=int(b/10)
count=count+a
b=b-(a*10)
count=count+b
print(count)
