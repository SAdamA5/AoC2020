input = []
with open("Advent12Input.txt") as file:
    for x in file:
        input.append(x.strip())

posY = 0 #N-S
posX = 0 #E-W
facing = 0 #0=East,3=North,2=West,1=South
#rigth turn will add to this value, left turn will substract from it

for command in input:
    order = command[0]
    degree = int(command[1:len(command)])
    if order == 'N':
        posY += degree
    elif order == 'S':
        posY -= degree
    elif order == 'E':
        posX += degree
    elif order == 'W':
        posX -= degree
    elif order == 'R':
        facing += (degree/90)
        facing = facing%4
    elif order == 'L':
        facing -= (degree/90)
        facing = facing%4
    elif order == 'F':
        if facing == 0:
            posX += degree
        elif facing == 1:
            posY -= degree
        elif facing == 2:
            posX -= degree
        elif facing == 3:
            posY += degree
        else:
            print('!!PORBLEM!!')

if posX<0:
    posX *= -1
if posY<0:
    posY *= -1

print(posY+posX)
    
wposX = 10
wposY = 1
posY = 0 
posX = 0 

for command in input:
    order = command[0]
    degree = int(command[1:len(command)])
    if order == 'N':
        wposY += degree
    elif order == 'S':
        wposY -= degree
    elif order == 'E':
        wposX += degree
    elif order == 'W':
        wposX -= degree
    elif order == 'R':
        for i in range(int(degree/90)):
            temp = wposY
            wposY = -1*wposX
            wposX = temp
    elif order == 'L':
       for i in range(int(degree/90)):
            temp = wposY
            wposY = wposX
            wposX = -1*temp
    elif order == 'F':
        for i in range(degree):
            posX += wposX
            posY += wposY


if posX<0:
    posX *= -1
if posY<0:
    posY *= -1

print(posY+posX)