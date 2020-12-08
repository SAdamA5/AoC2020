
input = []
with open("Advent8Input.txt") as file:
    for x in file:
        command = x.split()
        command = [command[0],int(command[1])]
        input.append(command)

accumulator = 0
executed = []
i = 0
run = True
while run:
    command = input[i]
    if i in executed:
        run = False
        break
    executed.append(i)
    if command[0]=='acc':
        accumulator += command[1]
        i += 1
    elif command[0] == 'nop':
        i += 1
    elif command[0] == 'jmp':
        i += command[1]

print(accumulator)

over = False
for i in range(len(input)):
    if input[i][0]=='acc':
        continue
    accumulator = 0
    executed = []
    j = 0
    run = True
    while run:
        command = input[j]
        executed.append(j)
        if j==i:
            if command[0] == 'nop':
                j += command[1]
            elif command[0] == 'jmp':
                j += 1
        if command[0]=='acc':
            accumulator += command[1]
            j += 1
        elif command[0] == 'nop':
            j += 1
        elif command[0] == 'jmp':
            j += command[1]
        else: ##I added a fin 0 line to the end of the file
            print(command)
            print(accumulator)
            over = True
        if j in executed:
            run = False
    if over:
        break
