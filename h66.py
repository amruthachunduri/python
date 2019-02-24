amu = int(raw_input())
arr = list(map(str,raw_input().split()))
p = raw_input()
count = 0
for i in arr:
    if(i.startswith(p)):
        count=count+1
print(count)
