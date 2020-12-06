input = []
with open("Advent6Input.txt") as file:
    string = ""
    for line in file:
        if len(line.strip()) == 0:
            input.append(string)
            string = ""
        else:
            string += line
    input.append(string)

answer1 = 0
for group in input:
    answers = group.split()
    saidYesTo = []
    for person in answers:
        person = person.strip()
        for letter in person:
            if letter not in saidYesTo:
                saidYesTo.append(letter)
    answer1 += len(saidYesTo)

print(answer1)

answer2 = 0
for group in input:
    answers = group.split()
    allSaidYesTo = []
    for i in range(len(answers)):
        person = answers[i].strip()
        if i==0:
            for letter in person:
                allSaidYesTo.append(letter)
        else:
            toRemove = []
            for letter in allSaidYesTo:
                if letter not in person:
                    toRemove.append(letter)
            for letter in toRemove:
                allSaidYesTo.remove(letter)
        if len(allSaidYesTo)==0:
            break
    answer2 += len(allSaidYesTo)
    

print(answer2)