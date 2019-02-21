_,k = map(int,raw_input().split(" "))
a = map(int,raw_input().split(" "))
l = len(a)
for __ in range(k):
    a = [a[l-1]] + a[0:l-1]
print " ".join(map(str,a))
