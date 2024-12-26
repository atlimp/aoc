#!/usr/bin/env python3

with open('input', 'r') as file:
    floor = 0
    for line in file.readlines():
        for i in range(len(line)):
            c = line[i]
            if c == '(':
                floor = floor + 1
            elif c == ')':
                floor = floor - 1
            
            if floor < 0:
                print(i + 1)
                break