def max(array):
    max = array[0]
    for i in array:
        if i>max:
            max = i
    return max
def min(array):
    min = array[0]
    for i in array:
        if i<min:
            min = i
    return min

input = []
with open('Advent9Input.txt') as file:
    for n in file:
        input.append(int(n))


for i  in range(25,len(input)):
    preamble = input[i-25:i]
    n = input[i]
    possible = False
    for x in range(len(preamble)-1):
        if possible:
            break
        for y in range(x+1,len(preamble)):
            a = preamble[x]
            b = preamble[y]
            if (a+b) == n:
                possible = True
                break
    if not possible:
        incorrect = n
        print(incorrect)


for i in range(len(input)):
    sum = input[i]
    delta = 0
    found = False
    while sum<incorrect:
        delta +=1
        sum += input[i+delta]
        if sum == incorrect:
            found = True
            break
    if found:
        break

weakness = input[i:i+delta+1]
print(max(weakness)+min(weakness))



