rules = []
myTicket = []
otherTickets = []

with open("Advent16Input.txt") as file:
    file = file.readlines()
    step = 0
    for i in range(len(file)):
        if step == 0:
            line = file[i].strip()
            if line == "":
                step += 1
                continue
            dummy = line.split(':')
            id = dummy[0].strip()
            dummy = dummy[1].split('or')
            lower = dummy[0].strip()
            upper = dummy[1].strip()
            dummy = lower.split('-')
            lowerMin = int(dummy[0].strip())
            lowerMax = int(dummy[1].strip())
            dummy = upper.split('-')
            upperMin = int(dummy[0].strip())
            upperMax = int(dummy[1].strip())
            rule = [id,lowerMin,lowerMax,upperMin,upperMax]
            rules.append(rule)
        elif step == 1:
            line = file[i].strip()
            numbs = line.split(',')
            if len(numbs) < 2:
                continue
            for n in numbs:
                myTicket.append(int(n))
            step += 1
        else:
            ticket = []
            line = file[i].strip()
            numbs = line.split(',')
            if len(numbs) < 2:
                continue
            for n in numbs:
                ticket.append(int(n))
            otherTickets.append(ticket)

lowerMin = rules[0][1]
lowerMax = rules[0][2]
upperMin = rules[0][3]
upperMax = rules[0][4]
connected = False
for i in range(1,len(rules)):
    if not(connected):
        rule = rules[i]
        if rule[1] < lowerMin:
            lowerMin = rule[1]
        if rule[2] > lowerMax:
            lowerMax = rule[2]
        if rule[3] < upperMin:
            upperMin = rule[3]
        if rule[4] > upperMax:
            upperMax = rule[4]
        if lowerMax >= upperMin:
            connected = True
    else:
        rule = rules[i]
        if rule[1] < lowerMin:
            lowerMin = rule[1]
        if rule[4] > upperMax:
            upperMax = rule[4]

scanningErrorRate = 0
toDiscard = []
if connected:
    for i in range(len(otherTickets)):
        ticket = otherTickets[i]
        for n in ticket:
            if n< lowerMin or n > upperMax:
                scanningErrorRate += n
                toDiscard.append(i)
else:
    for i in otherTickets:
        ticket = otherTickets[i]
        for n in ticket:
            if n< lowerMin or n > upperMax or (n > lowerMax and n < upperMin):
                scanningErrorRate += n
                toDiscard.append(i)

print(scanningErrorRate)

possibilities = []
nOfTicFi = len(myTicket)
ticketPlaces = []
for i in range(nOfTicFi):
    matchingFields = []
    for j in range(len(otherTickets)):
        if j in toDiscard:
            continue
        else:
            ticket = otherTickets[j]
            matchingFields.append(ticket[i])
    ticketPlaces.append(matchingFields)

for rule in rules:
    id = rule[0]
    lowerMin = rule[1]
    lowerMax = rule[2]
    upperMin = rule[3]
    upperMax = rule[4]
    for i in range(len(ticketPlaces)):
        matchingFields = ticketPlaces[i]
        possible = True
        for n in matchingFields:
            if n< lowerMin or n > upperMax or (n > lowerMax and n < upperMin):
                possible = False
                break
        if possible:
            possibilities.append([id,i])


possibilities.append(["dummy",-1]) ## so the folowing loop works correctly if the single is at the end
end = {}
while len(end)<20:
    single = []
    previous = ""
    n = 0
    for possibility in possibilities:
        if previous == possibility[0]:
            n += 1
            previous = possibility[0]
            previousNum = possibility[1]
        else:
            if n == 1:
                single.append(previous)
                single.append(previousNum)
                break
            n = 1
            previous = possibility[0]
            previousNum = possibility[1]

    end.update({single[0]:single[1]})
    toPop = []
    for i in range(len(possibilities)):
        possibility = possibilities[i]
        if possibility[0] == single[0] or possibility[1] == single[1]:
            toPop.append(i)


    for i in range(len(toPop)-1,-1,-1):
        popped = toPop[i]
        possibilities.pop(popped)

coord = []
coord.append(end['departure location'])
coord.append(end['departure station'])
coord.append(end['departure platform'])
coord.append(end['departure track'])
coord.append(end['departure date'])
coord.append(end['departure time'])

mul = 1
for c in coord:
    mul *= myTicket[c]

print(mul)



