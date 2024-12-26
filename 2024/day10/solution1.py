class Position:
    def __init__(self, height):
        self.height = height
        self.score = 0

class Map:
    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.map = []

        for line in input.split('\n'):
            heights = list(map(Position, list(map(int, list(line)))))
            self.map.append(heights)

    def solve(self):

        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                pos = self.map[row][col]
                if (pos.height == 0):
                    nines = self.traverse(row, col, -1)
                    pos.score = len(nines)

        
        sum = 0
        for row in self.map:
            for pos in row:
                sum = sum + pos.score
        
        return sum

    def traverse(self, row, col, prev_height):
        if not (row >= 0 and row < len(self.map) and col >= 0 and col < len(self.map[0])):
            return set()
        

        pos = self.map[row][col]

        if (prev_height + 1 != pos.height):
            return set()
        
        if (pos.height == 9):
            a = set()
            a.add((row, col))
            return a
        
        #NORTH
        nines = self.traverse(row - 1, col, pos.height)
        #EAST
        nines.update(self.traverse(row, col + 1, pos.height))
        #SOUTH
        nines.update(self.traverse(row + 1, col, pos.height))
        #WEST
        nines.update(self.traverse(row, col - 1, pos.height))

        return nines


    def __str__(self):
        s = ''
        for row in self.map:
            for col in row:
                s = s + f'{col.height}'
            s = s + '\n'
        return s

if __name__ == '__main__':
    file = open('input', 'r')
    a = Map(file.read())
    print(a)
    print(a.solve())
