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
    firstIndex = minCondition - 1
    code = dummy[1]
    dummy = code.split()
    maxCondition = int(dummy[0])
    secondIndex = maxCondition - 1
    req = dummy[1]
    good = False
    if password[minCondition]==req:
        good = True
    if good:
        if password[maxCondition]==req:
            good = False
    else:
        if password[maxCondition]==req:
            good = True
    if good:
        valid += 1

print(valid)
