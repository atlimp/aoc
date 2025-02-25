import re

ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

with open('input') as file:
    sues = []

    lines = file.read().split('\n')

    for line in lines:
        rest = re.sub('Sue [0-9]+: ', '', line)
        attributes = rest.split(', ')
        sue = {

        }

        for attribute in attributes:
            key, score = attribute.split(': ')
            sue[key] = int(score)
        
        sues.append(sue)
    
    for i in range(len(sues)):
        sue = sues[i]
        valid_sue = True
        for key in sue.keys():
            if key == 'cats' or key == 'trees':
                if ticker_tape[key] > sue[key]:
                    valid_sue = False
            elif key == 'pomeranians' or key == 'goldfish':
                if ticker_tape[key] < sue[key]:
                    valid_sue = False
            elif ticker_tape[key] != sue[key]:
                valid_sue = False
                break
        
        if valid_sue:
            print(i + 1)
            break
