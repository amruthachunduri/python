amu=str(raw_input())
for x in range(1,len(amu)):
    if amu[x:]>amu:
        print(amu[x:])
        break
