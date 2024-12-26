#!/usr/bin/env python3

with open('input', 'r') as file:
    sum = 0
    for line in file.readlines():
        l, w, h = map(int, line.split('x'))

        lw = l * w
        lh = l * h
        wh = w * h

        sum = sum + 2 * lw + 2 * lh + 2 * wh + min([lw, lh, wh])


    
    print(sum)
