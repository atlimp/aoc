def main():
    file = open('input', 'r')
    
    pos = 50
    zero_counter = 0
    for line in file:
        direction = line[0]
        num = int(line[1::])

        if direction == 'L':
            pos = pos - num
        elif direction == 'R':
            pos = pos + num
        
        pos = pos % 100

        if pos == 0:
            print('pos is ', pos)
            zero_counter = zero_counter + 1

    
    print(zero_counter)


if __name__ == '__main__':
    main()