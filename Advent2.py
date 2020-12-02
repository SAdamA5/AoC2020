file = open('Advent2Input.txt')
lines = []
for x in file:
    lines.append(x)


valid = 0

for line in lines:
    dummy = line.split(':')
    code = dummy[0]
    password = dummy[1]
    dummy = code.split('-')
    minCondition = int(dummy[0])
    code = dummy[1]
    dummy = code.split()
    maxCondition = int(dummy[0])
    req = dummy[1]
    counter = 0
    for p in password:
        if p==req:
            counter += 1
    if counter >= minCondition and counter <= maxCondition:
        valid += 1
    
print(valid)
    
