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
            print(col, end='')
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

with open('input.txt', 'r') as file:
  for line in file:
      grid.append(list(line))

# for line in inp.split('\n'):
#     grid.append(list(line))

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == '^':
            pos_x = j
            pos_y = i


while True:
    x, y = next_pos(pos_x, pos_y, dir)
    if (is_onscreen(grid, x, y)):
        if grid[y][x] == '#':
            # Turn
            dir = (dir + 1) % 4
        else:
            grid[pos_y][pos_x] = 'X'
            pos_x = x
            pos_y = y
            grid[pos_y][pos_x] = 'X'
    else:
        break

sum = 0
for row in grid:
    for col in row:
        if col == 'X':
            sum = sum + 1


printgrid()
print(sum)
