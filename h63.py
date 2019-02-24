amu = int(raw_input(""))
arr = list(map(int,raw_input().split()))
k =[]
for x in range(amu-1):
    j = max(arr[x+1:])
    k.append(str(j))
k.append(str(0))
print(" ".join(map(str,k)))
