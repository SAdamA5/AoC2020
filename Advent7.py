class Bag:
    def __init__(self, color, contains):
        self.color = color
        self.contains = contains

    def __str__(self):
        end = self.color +' contains: '
        for bag in self.contains:
            end += bag +'; '
        return end
###########################################################
def getBag(colour, array):
    for bag in array:
        if bag.color == colour:
            return bag

def hasShinyGold(bag, array, array1): #array = containers in later code, array1 = bags
    if bag.color not in array:
        return False
    elif ('shiny gold') in bag.contains:
        return True
    else:
        ans = False
        for innerBag in bag.contains:
            if innerBag in array:
                innerBag = getBag(innerBag,array1)
                if hasShinyGold(innerBag,array,array1):
                    ans = True
                    break
        if ans:
            return True
        else:
            return False


###########################################################
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
    for bag in innerBags:
        bag = bag.strip()
        bag = bag.split()
        bag = bag[1]+' '+bag[2]
        iBags.append(bag)
    bag = Bag(outerBag,iBags)
    bags.append(bag)


containers = [] #Ones that contain any colour
for bag in bags:
    containers.append(bag.color)
#print(containedColors)


answer1 = 0 
for colour in containers:
    theBag = getBag(colour,bags)   
    if hasShinyGold(theBag,containers,bags):
        answer1 += 1

print(answer1)





