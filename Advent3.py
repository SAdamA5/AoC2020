input=[]
with open("Advent3Input") as file:
    for x in file:
        input.append(x.strip())

width = len(input[0])
##R3 D1
x = 0 ##pos in line
trees3 = 0
for line in input:
    place = line[x]
    if place == '#':
        trees3 += 1
    x += 3
    if x >= width:
        x -= width
print(trees3)
##R1 D1
x = 0 ##pos in line
trees1 = 0
for line in input:
    place = line[x]
    if place == '#':
        trees1 += 1
    x += 1
    if x >= width:
        x -= width
print(trees1)
##R5 D1
x = 0 ##pos in line
trees5 = 0
for line in input:
    place = line[x]
    if place == '#':
        trees5 += 1
    x += 5
    if x >= width:
        x -= width
print(trees5)
##R7 D1
x = 0 ##pos in line
trees7 = 0
for line in input:
    place = line[x]
    if place == '#':
        trees7 += 1
    x += 7
    if x >= width:
        x -= width
print(trees7)
##R1 D2
x = 0 ##pos in line
c = 1
trees = 0
for line in input:
    c += 1
    if c%2 == 1:
        continue
    place = line[x]
    if place == '#':
        trees += 1
    x +=1
    if x >= width:
        x -= width
print(trees)

print(trees*trees1*trees3*trees5*trees7)