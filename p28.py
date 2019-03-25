amu=int(raw_input())
arr=list(map(int,raw_input().split()))
s=0
arr.sort()
for i in range(0,amu-1):
    s=s+arr[i] 
    if(s>arr[i+1]):
        break
print(i+2)
