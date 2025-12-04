class Floor:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        self.grid = []
        for line in lines:
            self.grid.append(list(line))

    def valid_index(self, row, col):
        return row >= 0 and row < len(self.grid) and col >= 0 and col < len(self.grid[0])
        
    def count_neighbors(self, row, col):
        count = 0
        #N
        n_row = row - 1
        n_col = col
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1
        
        #NE
        n_row = row - 1
        n_col = col + 1
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1
            
        #E
        n_row = row
        n_col = col + 1
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1
            
        #SE
        n_row = row + 1
        n_col = col + 1
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1
            
        #S
        n_row = row + 1
        n_col = col
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1
            
        #SW
        n_row = row + 1
        n_col = col - 1
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1
            
        #W
        n_row = row
        n_col = col - 1
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1

        #NW
        n_row = row - 1
        n_col = col - 1
        if self.valid_index(n_row, n_col) and self.grid[n_row][n_col] in ['@', 'x']:
            count += 1

        return count

    def solve(self):
        sum = 0
        removed = 1
        while removed > 0:
            removed = 0
            for i in range(len(self.grid)):
                row = self.grid[i]
                for j in range(len(row)):
                    token = self.grid[i][j]
                    if token == '@':
                        if self.count_neighbors(i, j) < 4:
                            self.grid[i][j] = 'x'
                            removed += 1

            print(self)
            self.purge()
            sum += removed

        return sum

    def purge(self):
        for i in range(len(self.grid)):
            row = self.grid[i]
            for j in range(len(row)):
                token = self.grid[i][j]
                if token == 'x':
                    self.grid[i][j] = '.'

    def __str__(self):
        string = ''
        for row in self.grid:
            for col in row:
                string += col
            string += '\n'
        
        return string


if __name__ == '__main__':
    file = open('input', 'r')
    a = Floor(file.read())
    print(a.solve())