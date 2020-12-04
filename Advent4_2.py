def hasReqFields(keys):
    valid = True
    if 'byr'  not in keys:
        valid = False
    elif 'iyr' not in keys:
        valid = False
    elif 'eyr' not in keys:
        valid = False
    elif 'hgt' not in keys:
        valid = False
    elif 'hcl' not in keys:
        valid = False
    elif 'ecl' not in keys:
        valid = False
    elif 'pid' not in keys:
        valid = False
    return valid

def BYRvalid(byr):
    byr = int(byr)
    if byr>= 1920 and byr<=2020:
        return True
    return False

def IYRvalid(iyr):
    iyr = int(iyr)
    if iyr>=2010 and iyr<=2020:
        return True
    return False

def EYRvalid(eyr):
    eyr = int(eyr)
    if eyr >=2020 and eyr <= 2030:
        return True
    return False

def HGTvalid(hgt):
    measure = hgt[-1]
    if measure == 'n': #inch
        amount = int(hgt.split('i')[0])
        if amount >= 59 and amount <= 76:
            return True
    elif measure == 'm': #cm
        amount = int(hgt.split('c')[0])
        if amount >= 150 and amount <= 193:
            return True
    else:
        return False

def HCLvalid(hcl):
    if hcl[0] != '#':
        return False
    chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(len(hcl)):
        if i == 0:
            continue
        if hcl[i] not in chars:
            return False
    return True

def ECLvalid(ecl):
    colors = ['amb','blu','brn','gry','grn','hzl','oth']
    if ecl in colors:
        return True
    return False

def PIDvalid(pid):
    nums = ['0','1','2','3','4','5','6','7','8','9']
    if len(pid) != 9:
        return False
    for n in pid:
        if n not in nums:
            return False
    return True 


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

persons = []

for s in input:
    dic = {}
    data = s.split()
    for d in data:
        dummy = d.split(':')
        dic.update({dummy[0]:str(dummy[1])})
    persons.append(dic)

answer = 0

for person in persons:
    if(hasReqFields(person.keys())):
        if(BYRvalid(person.get('byr')) and IYRvalid(person.get('iyr')) and EYRvalid(person.get('eyr')) and HGTvalid(person.get('hgt')) and HCLvalid(person.get('hcl')) and ECLvalid(person.get('ecl')) and PIDvalid(person.get('pid'))):
            answer += 1
print(answer)


    