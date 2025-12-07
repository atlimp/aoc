class Beam:
    def __init__(self, input):
        self.cache = {}
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        
        self.grid = []
        for line in lines:
            self.grid.append(list(line))
        

    def split(self, row, col):
        key = f'{row}_{col}'
        if key in self.cache:
            return self.cache[key]

        if row >= len(self.grid):
            return 0
        
        if self.grid[row][col] == '^': #split
            result = 1 + self.split(row, col - 1) + self.split(row, col + 1)
            self.cache[key] = result
            return result

        result = self.split(row + 1, col)
        self.cache[key] = result
        return result

    def solve(self):
        starting_index = self.grid[0].index('S')
        self.grid[1][starting_index] = '|'
        
        return self.split(1, starting_index) + 1
    
    def __str__(self):
        string = ''
        for row in self.grid:
            for col in row:
                string += col
            string += '\n'
        
        return string



if __name__ == '__main__':
    file = open('input', 'r')
    a = Beam(file.read())
    print(a.solve())