NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


inp = '....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...'

grid = []
pos_x = 0
pos_y = 0

dir = 0


def printgrid():
    for row in grid:
        for col in row:
            print(col[0], end='')
        print()

def next_pos(x, y, dir):
    if (dir == NORTH):
        return (x, y - 1)
    if (dir == EAST):
        return (x + 1, y)
    if (dir == SOUTH):
        return (x, y + 1)
    if (dir == WEST):
        return (x - 1, y)
    return

def is_onscreen(arr, x, y):
    return x >= 0 and x < len(arr[0]) and y >= 0 and y < len(arr)

def reload_grid():
    global pos_x, pos_y
    board = []
    with open('input.txt', 'r') as file:
      for line in file:
          board.append(list(line))

    # for line in inp.split('\n'):
    #     board.append(list(line))

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            board[i][j] = [board[i][j], -1]
            if board[i][j][0] == '^':
                pos_x = j
                pos_y = i
    
    return board
    


grid = reload_grid()
break_counter_list = []
valid_spot = 0
print_grid = False
for i in range(0, len(grid)):
    print(f'{i}/{len(grid)}')
    for j in range(0, len(grid[i])):
        if grid[i][j][0] == '^' or grid[i][j][0] == '#':
            continue

        #print(f'{j}/{len(grid[0])}')


        grid[i][j][0] = 'O'

        counter = 0
        hit_counter = {}
        while True:
            x, y = next_pos(pos_x, pos_y, dir)
            if (is_onscreen(grid, x, y)):
                token, old_dir = grid[y][x]
                if token == '#' or token == 'O':
                    # Turn
                    dir = (dir + 1) % 4
                else:
                    if print_grid:
                        printgrid()
                    grid[pos_y][pos_x] = ['X', dir]
                    pos_x = x
                    pos_y = y
                    grid[pos_y][pos_x] = ['X', dir]

                
                if token == 'X':
                    key = f'{pos_x},{pos_y}'
                    if not key in hit_counter:
                        hit_counter[key] = 1
                    
                    hit_counter[key] = hit_counter[key] + 1


                    if hit_counter[key] > 4:
                        #Seen it before
                        valid_spot = valid_spot + 1
                        break
                    
            else:
                break
            
            counter = counter + 1
            if counter > 1000000:
                break_counter_list.append([j, i])
                print(f'break counter x: {j}, y: {i}')
                break
        
        grid = reload_grid()
        dir = 0



print(valid_spot)
