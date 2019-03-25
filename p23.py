N = 0
E = 1
S = 2
W = 3
def isCircular(amu):  
    x = 0
    y = 0
    dir = N 
    for i in range(len(amu)):
        move = amu[i] 
        if move == 'R': 
            dir = (dir + 1)%4
        elif move == 'L': 
            dir = (4 + dir - 1)%4
        else:
            if dir == N: 
                y += 1
            elif dir == E: 
                x += 1
            elif dir == S: 
                y -= 1
            else: 
                x -= 1
    return (x == 0 and y == 0) 
amu =(raw_input())
if isCircular(amu): 
    print ("yes")
else: 
    print("no")
