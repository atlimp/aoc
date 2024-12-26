NORTH = 0
NORTHEAST = 1
EAST = 2
SOUTHEAST = 3
SOUTH = 4
SOUTHWEST = 5
WEST = 6
NORTHWEST = 7


#inp = '.M.S......\n..A..MSMS.\n.M.S.MAA..\n..A.ASMSM.\n.M.S.M....\n..........\nS.S.S.S.S.\n.A.A.A.A..\nM.M.M.M.M.\n..........'


grid = []


# for line in inp.split('\n'):
#     grid.append(list(line))

with open('input.txt', 'r') as file:
    for line in file:
       grid.append(list(line))

def canmatch(arr, row, col, word, direction):
    wordlen = len(word)
    maxrow = len(arr)
    maxcol = len(arr[0])

    if (col < 0 or col >= maxcol or row < 0 or row >= maxrow):
        return False

    if (direction == NORTH):
        if (row + 1 >= wordlen):
            return True
        return False
            
    elif (direction == EAST):
        if (col <= maxcol - wordlen):
            return True
        return False

            
    elif (direction == SOUTH):
        if (row <= maxrow - wordlen):
            return True
        return False

            
    elif (direction == WEST):
        if (col + 1 >= wordlen):
            return True
        return False

    if (direction == NORTHEAST):
        return canmatch(arr, row, col, word, NORTH) and canmatch(arr, row, col, word, EAST)
    if (direction == SOUTHEAST):
        return canmatch(arr, row, col, word, SOUTH) and canmatch(arr, row, col, word, EAST)
    if (direction == SOUTHWEST):
        return canmatch(arr, row, col, word, SOUTH) and canmatch(arr, row, col, word, WEST)
    if (direction == NORTHWEST):
        return canmatch(arr, row, col, word, NORTH) and canmatch(arr, row, col, word, WEST)

    return False

def matchword(arr, row, col, word, direction):

    if (not canmatch(arr, row, col, word, direction)):
        return False

    coloff = 0
    rowoff = 0
    for i in range(0, len(word)):
        char = word[i]
        token = arr[row + rowoff][col + coloff]

        if (char != token):
            return False

        if (direction == NORTH or direction == NORTHEAST or direction == NORTHWEST):
            rowoff = rowoff - 1

        if (direction == EAST or direction == NORTHEAST or direction == SOUTHEAST):
            coloff = coloff + 1

        if (direction == SOUTH or direction == SOUTHEAST or direction == SOUTHWEST):
            rowoff = rowoff + 1

        if (direction == WEST or direction == NORTHWEST or direction == SOUTHWEST):
            coloff = coloff - 1

    return True

word_to_match = 'MAS'
word_to_match_rev = word_to_match[::-1]
matches = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if ((matchword(grid, row, col, word_to_match, SOUTHEAST) or matchword(grid, row, col, word_to_match_rev, SOUTHEAST))
            and (matchword(grid, row, col + 2, word_to_match, SOUTHWEST) or matchword(grid, row, col + 2, word_to_match_rev, SOUTHWEST))
        ):
            matches = matches + 1

print(matches)