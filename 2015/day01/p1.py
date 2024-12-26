#!/usr/bin/env python3

with open('input', 'r') as file:
    floor = 0
    for line in file.readlines():
        for c in list(line):
            if c == '(':
                floor = floor + 1
            elif c == ')':
                floor = floor - 1

    
    print(floor)
