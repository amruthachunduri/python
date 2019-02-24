amu=raw_input()
for j in range(0,len(amu)):
    k=amu[:j]+amu[j+1:]

    if(k[:]==k[::-1]):
    
        print("YES")
        break
else:
    print("NO")
