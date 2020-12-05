def halfArray(array,x=0):
    l = len(array)
    length = int(l/2)
    start = x*length ## x==1 if second half
    ret = []
    for i in range(length):
        ret.append(array[start])
        start +=1 
    return ret


input = []
with open('Advent5Input.txt') as file:
    for x in file:
        input.append(x.strip())
rows = []
for x in range(128):
    rows.append(x)
collums = []
for x in range(8):
    collums.append(x)

answer1 = 0
ids = []
for bpass in input:
    prows = rows.copy()
    for i in range(7):
        if bpass[i] == 'F':
            prows = halfArray(prows)
        else:
            prows = halfArray(prows,1)
    pcols = collums.copy()
    for i in range (3):
        if bpass[7+i] == 'L':
            pcols=halfArray(pcols)
        else:
            pcols=halfArray(pcols,1)
    row = prows[0]
    col = pcols[0]
    id = row*8+col
    ids.append(id)
    if id>answer1:
        answer1 = id

print('Highest id: '+str(answer1))


for i in range(answer1):
    previous = i-1
    next = i+1
    if i not in ids:
        if (previous in ids) and (next in ids):
            print('A possible missing id: '+str(i))


