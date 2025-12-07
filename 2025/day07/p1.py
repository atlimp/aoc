class Beam:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        
        self.grid = []
        for line in lines:
            self.grid.append(list(line))
        
        print(self)


    def solve(self):
        splits = 0
        starting_index = self.grid[0].index('S')
        self.grid[1][starting_index] = '|'
        for i in range(len(self.grid) - 1):
            row = self.grid[i]
            next_row = self.grid[i + 1]
            for j in range(len(row)):
                token = row[j]
                next_row_token = next_row[j]
                if token == '|':
                    if next_row_token == '^':
                        next_row[j - 1] = '|'
                        next_row[j + 1] = '|'
                        splits += 1
                    else:
                        next_row[j] = '|'

            print(self)
            print(splits)
        return splits
    
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