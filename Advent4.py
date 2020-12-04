input = []
with open("Advent4Input.txt") as file:
    string = ""
    for line in file:
        if len(line.strip()) == 0:
            input.append(string)
            string = ""
        else:
            string += line
    input.append(string)



answer = 0
for onePerson in input:
    data = onePerson.split()
    codes = []
    for oneData in data:
        dummy = oneData.split(':')
        codes.append(dummy[0])
    correct = True
    if 'byr'  not in codes:
        correct = False
    elif 'iyr' not in codes:
        correct = False
    elif 'eyr' not in codes:
        correct = False
    elif 'hgt' not in codes:
        correct = False
    elif 'hcl' not in codes:
        correct = False
    elif 'ecl' not in codes:
        correct = False
    elif 'pid' not in codes:
        correct = False
    if correct:
        answer +=1
    

print(answer)
