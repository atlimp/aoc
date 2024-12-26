class Antenna:
    def __init__(self, token, row, col):
        self.token = token
        self.row = row
        self.col = col

    def create_antinode(self, antenna):
        diff_row = self.row - antenna.row
        diff_col = self.col - antenna.col

        return Antenna('#', self.row + diff_row, self.col + diff_col)
    
    def copy(self):
        return Antenna(self.token, self.row, self.col)

    def __hash__(self):
        return self.row * 100 + self.col
    
    def __eq__(self, value):
        return self.row == value.row and self.col == value.col

    def __str__(self):
        return f'{self.token}:[{self.row}, {self.col}]'

class Map:
    def __init__(self, input):
        self.antennas = {}
        self.parse(input)
        self.size = len(self.grid)
    
    def parse(self, input):
        self.grid = []
        for line in input.split('\n'):
            self.grid.append(list(line))

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                token = self.grid[row][col]

                if token != '.':
                    antenna = Antenna(token, row, col)
                    
                    if (token not in self.antennas):
                        self.antennas[token] = []

                    self.antennas[token].append(antenna)

    def solve(self):
        self.antennas['#'] = []
        for token in self.antennas:
            if (token == '#'):
                continue
            antenna_list = self.antennas[token]
            for i in range(len(antenna_list)):
                for j in range(i, len(antenna_list)):
                    if (i == j):
                        continue
                    a = antenna_list[i]
                    b = antenna_list[j]

                    curr_antinode = a.create_antinode(b)
                    prev_antinode = a.copy()
                    while self.within_bounds(curr_antinode):
                        self.antennas['#'].append(curr_antinode)
                        self.grid[curr_antinode.row][curr_antinode.col] = '#'
                        prev_antinode = curr_antinode.create_antinode(prev_antinode)
                        prev_antinode, curr_antinode = curr_antinode, prev_antinode

                    curr_antinode = b.create_antinode(a)
                    prev_antinode = b.copy()
                    while self.within_bounds(curr_antinode):
                        self.antennas['#'].append(curr_antinode)
                        self.grid[curr_antinode.row][curr_antinode.col] = '#'
                        prev_antinode = curr_antinode.create_antinode(prev_antinode)
                        prev_antinode, curr_antinode = curr_antinode, prev_antinode
        
        all_antennas = set()
        for token in self.antennas:
            all_antennas.update(self.antennas[token])
        return len(all_antennas)

    def within_bounds(self, node):
        return node.col >= 0 and node.col < self.size and node.row >= 0 and node.row < self.size
    
    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s = s + col
            s = s + '\n'
        
        return s


if __name__ == '__main__':
    file = open('input', 'r')
    a = Map(file.read())
    #print(a)
    print(a.solve())
    #print(a)