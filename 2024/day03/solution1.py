import re

instructions = ''


with open('input', 'r') as file:
    for line in file:
        instructions = instructions + line


matches = re.findall('mul\(\d{1,3},\d{1,3}\)', instructions)

sum = 0
for match in matches:
    nums = re.findall('\d{1,3}', match)
    a = int(nums[0])
    b = int(nums[1])

    sum = sum + a * b

print(sum)
