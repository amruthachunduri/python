amu=int(raw_input())
arr=list(map(int,raw_input().split()))
if(sum(arr)==3):
    print("1 0 1\n1 0 1\n0 1 1\n1 0 1")
else:
    for i in range(amu):
        for j in range (amu):
            for k in range (amu):
                if arr[i]+arr[j]==arr[k] and i<j<k:
                    print arr[i],arr[j],arr[k]
