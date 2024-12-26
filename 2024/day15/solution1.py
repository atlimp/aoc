class Floor:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        map, moves = input.split('\n\n')

        self.grid = []
        for line in map.split('\n'):
            self.grid.append(list(line))
        
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
    
        if self.grid[new_row][new_col] == 'O':
            if self.move(new_row, new_col, row_off, col_off):
                self.grid[new_row][new_col] = self.grid[old_row][old_col]
                self.grid[old_row][old_col] = '.'
                return True
            
        return False

    
    
    def solve(self):
        for move in self.moves:
            #input(f'Move {move}:')
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

            #print(self)

        sum = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if (self.grid[row][col] == 'O'):
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
