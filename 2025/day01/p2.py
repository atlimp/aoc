def main():
    file = open('input', 'r')
    
    pos = 50
    zero_counter = 0
    for line in file:
        line = line.replace('\n', '')
        direction = line[0]
        num = int(line[1::])

        zero_count = 0
        if direction == 'L':
            new_pos = pos - num
            zero_count = int((new_pos - 100) * -1 / 100)
            if pos == 0:
                zero_count = zero_count - 1
            pos = new_pos % 100
        elif direction == 'R':
            new_pos = pos + num
            zero_count = int(new_pos / 100)
            pos = new_pos % 100
        
        print('line', line)
        print('pos', pos)
        print('zero', zero_count)
        zero_counter = zero_counter + zero_count

    
    print(zero_counter)


if __name__ == '__main__':
    main()