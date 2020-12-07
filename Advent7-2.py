class Bag:
    def __init__(self, color, contains, numbers):
        self.color = color
        self.contains = contains
        self.numbers = numbers

    def __str__(self):
        end = self.color +' contains: '
        for i in range(len(self.contains)):
            end += str(self.numbers[i])+' '+self.contains[i] +'; '
        return end
####################################################
def getBag(colour, array):
    for bag in array:
        if bag.color == colour:
            return bag

def numberOfBags(bag,array): # array = bags
    n = 0
    if bag.contains == None:
        return 1
    for i in range(len(bag.contains)):
        innerBag = (getBag(bag.contains[i],array))
        innerBagcontains = numberOfBags(innerBag,array)
        multiplier = bag.numbers[i]
        n += (multiplier*(innerBagcontains))
    return n+1


####################################################
input = []
with open('Advent7Input.txt') as file:
    for x in file:
        input.append(x.strip())

bags = []
for rule in input:
    rule = rule.split('bags contain')
    outerBag = rule[0].strip()
    innerBags = rule[1].split(',')
    iBags = []
    numbs = []
    contains = True
    for bag in innerBags:
        bag = bag.strip()
        bag = bag.split()
        addBag = bag[1]+' '+bag[2]
        iBags.append(addBag)
        if bag[0] == 'no':
            contains = False
        else:
            numbs.append(int(bag[0]))
    if contains:
        bag = Bag(outerBag,iBags,numbs)
        bags.append(bag)
    else:
        bag = Bag(outerBag,None,None)
        bags.append(bag)

   
print(numberOfBags(getBag('shiny gold',bags),bags))

