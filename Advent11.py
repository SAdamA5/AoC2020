def occAdjs(r, c, array):
    length = len(array)
    wide = len(array[0])
    u = r-1
    d = r+1
    ri = c+1
    l = c-1
    n = 0
    if u > -1:#upper
        if array[u][c] == '#':
            n += 1
    if d < length:#lower
        if array[d][c] == '#':
            n += 1
    if ri < wide:#right-hand-side
        if array[r][ri] == '#':
            n += 1
    if l >- 1:#left-hand-side
        if array[r][l] == '#':
            n += 1
    if u > -1 and l > -1:#upper-left
        if array[u][l] == '#':
            n += 1
    if u > -1 and ri < wide:#upper-right
        if array[u][ri] == '#':
            n += 1
    if d < length and l > -1:#lower-left
        if array[d][l] == '#':
            n += 1
    if d < length and ri < wide:#lower-right
        if array[d][ri] == '#':
            n += 1
    return n

def occAdjsFar(r,c,array):
    length = len(array)
    wide = len(array[0])
    u = r-1
    d = r+1
    ri = c+1
    l = c-1
    n = 0
    while u > -1:#upper
        if not(array[u][c] == '.'):
            if array[u][c] == '#':
                n += 1
            break
        u -= 1
    while d < length:#lower
        if not(array[d][c] == '.'):
            if array[d][c] == '#':
                n += 1
            break
        d += 1
    while ri < wide:#right-hand-side
        if not(array[r][ri] == '.'):
            if array[r][ri] == '#':
                n += 1
            break
        ri += 1
    while l >- 1:#left-hand-side
        if not(array[r][l] == '.'):
            if array[r][l] == '#':
                n += 1
            break
        l -= 1
    u = r-1
    ri = c+1
    l = c-1
    while u > -1 and l > -1:#upper-left
        if not(array[u][l] == '.'):
            if array[u][l] == '#':
                n += 1
            break
        u -= 1
        l -= 1
    u = r-1
    while u > -1 and ri < wide:#upper-right
        if not(array[u][ri] == '.'):
            if array[u][ri] == '#':
                n += 1
            break
        u -= 1
        ri += 1
    d = r+1
    ri = c+1
    l = c-1
    while d < length and l > -1:#lower-left
        if not(array[d][l] == '.'):
            if array[d][l] == '#':
                n += 1
            break
        d += 1
        l -= 1
    d = r+1
    while d < length and ri < wide:#lower-right
        if not(array[d][ri] == '.'):
            if array[d][ri] == '#':
                n += 1
            break
        d += 1
        ri += 1
    return n

def changeStrChar(index, char, str):
    end = ""
    for i in range(len(str)):
        if i == index:
            end += char
        else:
            end += str[i]
    return end

def simulateChange(array, limit, second = False):
    toChange = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 'L':
                if second:
                    if occAdjsFar(i,j,array)==0:
                        toChange.append([i,j])
                else:
                    if occAdjs(i,j,array)==0:
                        toChange.append([i,j])
            elif array[i][j] == '#':
                if second:
                    if occAdjsFar(i,j,array)>=limit:
                        toChange.append([i,j])
                else:
                    if occAdjs(i,j,array)>=limit:
                        toChange.append([i,j])
    for coord in toChange:
        if array[coord[0]][coord[1]] == 'L':
            array[coord[0]] = changeStrChar(coord[1],'#',array[coord[0]])
        elif array[coord[0]][coord[1]] == '#':
            array[coord[0]] = changeStrChar(coord[1],'L',array[coord[0]])

def getOccupied(array, char):
    n = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]==char:
                n += 1
    return n



input = []
with open("Advent11Input.txt") as file:
    for x in file:
        input.append(x.strip())

previous = -1
current = 0
while previous != current:
    simulateChange(input,4)
    previous = current
    current = getOccupied(input, '#')

print(current)

input = []
with open("Advent11Input.txt") as file:
    for x in file:
        input.append(x.strip())

previous = -1
current = 0
while previous != current:
    simulateChange(input,5, True)
    previous = current
    current = getOccupied(input, '#')

print(current)

