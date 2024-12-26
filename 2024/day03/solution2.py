import re

def tryparsemul(s, i):


    if (s[i:i + 3] != 'mul'):
        return 0
    
    i = i + 3

    candidate = s[i:i + 9]
    match = re.match('\(\d{1,3},\d{1,3}\)', candidate)
    if (match):
        nums = re.findall('\d{1,3}', match.string)
        a = int(nums[0])
        b = int(nums[1])
        return a * b

    return 0

enabled = True

instructions = ''#mul(2,2)do()mul(1,3)don\'t()mul(3,3)sdfljksdfmul(32,23)do()sdflsdfljmul(1,2)'


with open('input', 'r') as file:
    for line in file:
        instructions = instructions + line


sum = 0
for i in range(0, len(instructions)):
    token = instructions[i]
    
    if (token == 'm' and enabled):
        prod = tryparsemul(instructions, i)
        sum = sum + prod
        continue

    if (token == 'd'):
        if (instructions[i:i + 4] == 'do()'):
            enabled = True
        if (instructions[i:i + 7] == 'don\'t()'):
            enabled = False



print(sum)
