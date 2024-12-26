class Floor:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        map, moves = input.split('\n\n')

        self.grid = []
        for line in map.split('\n'):
            self.grid.append([])
            grid_line = self.grid[len(self.grid) - 1]
            for token in list(line):
                if token == '#':
                    grid_line.append('#')
                    grid_line.append('#')
                if (token == 'O'):
                    grid_line.append('[')
                    grid_line.append(']')
                if (token == '.'):
                    grid_line.append('.')
                    grid_line.append('.')
                if (token == '@'):
                    grid_line.append('@')
                    grid_line.append('.')
        
        self.moves = list(moves.replace('\n', ''))

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == '@':
                    self.robot_col = col
                    self.robot_row = row
                    return

    
    def move(self, old_row, old_col, row_off, col_off):
        new_row = old_row + row_off
        new_col = old_col + col_off

        if self.grid[new_row][new_col] == '#':
            return False
        
        if self.grid[new_row][new_col] == '.':
            self.grid[new_row][new_col] = self.grid[old_row][old_col]
            self.grid[old_row][old_col] = '.'
            return True
    
        if self.grid[new_row][new_col] == '[' or self.grid[new_row][new_col] == ']':
            if row_off == 0: #HORIZONTAL
                if self.can_move(new_row, new_col, row_off, col_off):
                    self.move(new_row, new_col, row_off, col_off)
                    self.grid[new_row][new_col] = self.grid[old_row][old_col]
                    self.grid[old_row][old_col] = '.'
                    return True
            else:
                token = self.grid[new_row][new_col]

                if (token == '['):
                    if self.can_move(new_row, new_col, row_off, col_off) and self.can_move(new_row, new_col + 1, row_off, col_off):
                        self.move(new_row, new_col, row_off, col_off)
                        self.move(new_row, new_col + 1, row_off, col_off)
                        self.grid[new_row][new_col] = self.grid[old_row][old_col]
                        self.grid[old_row][old_col] = '.'
                        return True
                elif (token == ']'):
                    if self.can_move(new_row, new_col, row_off, col_off) and self.can_move(new_row, new_col - 1, row_off, col_off):
                        self.move(new_row, new_col, row_off, col_off)
                        self.move(new_row, new_col - 1, row_off, col_off)
                        self.grid[new_row][new_col] = self.grid[old_row][old_col]
                        self.grid[old_row][old_col] = '.'
                        return True
            
        return False
    
    def can_move(self, old_row, old_col, row_off, col_off):
        new_row = old_row + row_off
        new_col = old_col + col_off

        if self.grid[new_row][new_col] == '#':
            return False
        
        if self.grid[new_row][new_col] == '.':
            return True
    
        if self.grid[new_row][new_col] == '[' or self.grid[new_row][new_col] == ']':
            if row_off == 0: #HORIZONTAL
                if self.can_move(new_row, new_col, row_off, col_off):
                    return True
            else:
                token = self.grid[new_row][new_col]

                if (token == '['):
                    if self.can_move(new_row, new_col, row_off, col_off) and self.can_move(new_row, new_col + 1, row_off, col_off):
                        return True
                elif (token == ']'):
                    if self.can_move(new_row, new_col, row_off, col_off) and self.can_move(new_row, new_col - 1, row_off, col_off):
                        return True
            
        return False
    
    

    
    
    def solve(self):
        for move in self.moves:
            #input('move')
            if (move == '^'):
                if self.move(self.robot_row, self.robot_col, -1, 0):
                    self.robot_row = self.robot_row - 1

            elif (move == '>'):
                if self.move(self.robot_row, self.robot_col, 0, 1):
                    self.robot_col = self.robot_col + 1
            
            elif (move == 'v'):
                if self.move(self.robot_row, self.robot_col, 1, 0):
                    self.robot_row = self.robot_row + 1

            elif (move == '<'):
                if self.move(self.robot_row, self.robot_col, 0, -1):
                    self.robot_col = self.robot_col - 1

            go_up = '\033[F' * (len(self.grid) + 1)

            print(f'{go_up}{self}')

        sum = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if (self.grid[row][col] == '['):# or self.grid[row][col] == ']'):
                    sum = sum + row * 100 + col

        return sum


    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s = s + col
            
            s = s + '\n'
        
        return s
    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Floor(file.read())
    print(a)
    print(a.solve())
