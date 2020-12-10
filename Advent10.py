from itertools import combinations

def Sort(array):
    for x in range(len(array)-1):
        for y in range(len(array)-x-1):
            a = array[y]
            b = array[y+1]
            if a>b:
                array[y] = b
                array[y+1] = a

def getPossible(array):
    n = len(array)
    x = 1 ##keeping it all
    #print(x)
    if n>1:
        x += n-2 ##removing one from the middle
        #print(x)
    if n>3:
        dummy = []
        for i in range(1,len(array)-1):
            dummy.append(array[i])
        x += len(list(combinations(dummy,2))) ## removing two from the middle
        #print(x)
    # if there is a five long, you cannot remove all three from the middle, because than you would have
    # a 4 gap
    return x
    
    

input = []
with open('Advent10Input.txt') as file:
    for x in file:
        input.append(int(x.strip()))

Sort(input)
input.append((input[-1]+3))

n1 = 0
n2 = 0
n3 = 0
a = input[0]
if a == 1:
    n1 += 1
elif a == 2:
    n2 += 1
elif a == 3:
    n3 += 1
for i in range(len(input)-1):
    a = input[i]
    b = input[i+1]
    c = b-a
    if c == 1:
        n1 += 1
    elif c == 2:
        n2 += 1
    elif c == 3:
        n3 += 1


print(n1*n3)

#only works if there are no two differences
oneDiffLists = []
jigsaw = []
for i in range(len(input)-1):
    a = input[i]
    b = input[i+1]
    if (b-a) == 1:
        jigsaw.append(a)
    else:
        jigsaw.append(a)
        oneDiffLists.append(jigsaw)
        jigsaw = []
#only works if the oneDiffLists' biggest jigsaw array is 5 long
print(oneDiffLists)


n = 1
first = oneDiffLists[0]
fMult = getPossible(first)
if 1 in first and len(first)>1:
    fMult += 1
if 2 in first and 1 not in first:
    fMult += 1
if 1 in first and 2 in first:
    fMult += 1
n *= fMult
print(n)
for i in range(1,len(oneDiffLists)):
    jigsaw = oneDiffLists[i]
    print(getPossible(jigsaw))
    n *= getPossible(jigsaw)

print(n)


