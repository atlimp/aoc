#!/usr/bin/env python3

with open('input', 'r') as file:
    sum = 0
    for line in file.readlines():
        l, w, h = map(int, line.split('x'))

        lw = l * 2 + w * 2
        lh = l * 2 + h * 2
        wh = w * 2 + h * 2
        vol = l * w * h

        sum = sum + vol + min([lw, lh, wh])


    
    print(sum)
