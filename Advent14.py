def changeChar(string, index, to):
    result = ""
    for i in range(len(string)):
        if i==index:
            result += to
        else:
            result += string[i]
    return result

def decToBin(x):
    power = 0
    while 2**power<x:
        power += 1
    power -= 1
    result = ""
    while power>-1:
        if x >= 2**power:
            result += "1"
            x -= 2**power
            power -= 1
        else:
            result += "0"
            power -= 1
    return result

def make36bits(bin):
    zeros = 36-len(bin)
    result = ""
    for i in range(zeros):
        result += "0"
    for i in bin:
        result += i
    return result

def Mask(bin,mask):
    result = ""
    for i in range(len(bin)):
        if mask[i] == "X":
            result += bin[i]
        elif mask[i] =='0':
            result += '0'
        elif mask[i] == '1':
            result += '1'
    return result

def binToDec(bin):
    result = 0
    power = 0
    for b in reversed(bin):
        if b == '1':
            result += 2**power
        power +=1
    return result

def addressMask(bin,mask):
    result = ""
    for i in range(len(mask)):
        if mask[i] == '0':
            result += bin[i]
        elif mask[i] == '1':
            result += '1'
        elif mask[i] == 'X':
            result += 'X'
    return result

def makeAddress(maskedAddress,result = []):
    for i in range(len(maskedAddress)):
        if maskedAddress[i] == 'X':
            result.append(makeAddress(changeChar(maskedAddress,i,'0'),result)) 
            result.append(makeAddress(changeChar(maskedAddress,i,'1'),result))
            return result
    return result.append(maskedAddress)

def correct(array):
    end = []
    for x in array:
        if(isinstance(x,str)):
            end.append(x)
    return end

def doMemoryUpdate(memory, adresses, value):
    for adress in adresses:
        memory.update({adress:value})

with open("Advent14Input.txt") as file:
    input = file.readlines()
    for i in range(len(input)):
        input[i] = input[i].strip()

mask = ""
memory = {}
for line in input:
    dummy = line.split('=')
    command = dummy[0].strip()
    code = dummy[1].strip()
    if command == 'mask':
        mask = code
    else:
        dummy = command.split('[')
        place = int(dummy[1].split(']')[0].strip())
        code = int(code)
        masked = Mask(make36bits(decToBin(code)),mask)
        memory.update({place:binToDec(masked)})

sum = 0
for key in memory:
    sum += memory[key]

print(sum)

with open("Advent14Input.txt") as file:
    input = file.readlines()
    for i in range(len(input)):
        input[i] = input[i].strip()

mask = ""
memory = {}
for line in input:
    
    dummy = line.split('=')
    command = dummy[0].strip()
    code = dummy[1].strip()
    if command == 'mask':
        mask = code
    else:
        dummy = command.split('[')
        place = make36bits(decToBin(int(dummy[1].split(']')[0].strip())))
        code = int(code)
        masked = Mask(make36bits(decToBin(code)),mask)
        maskedAddress = addressMask(place,mask)
        adresses = correct(makeAddress(maskedAddress,result = []))
        for i in range(len(adresses)):
            adresses[i] = binToDec(adresses[i])
        doMemoryUpdate(memory,adresses,code)


sum = 0
for key in memory:
    sum += memory[key]

print(sum)
