amu,abi=list(map(int,raw_input().split()))
x=0
while(amu>=abi):
    amu-=abi
    x+=1
print(x)
