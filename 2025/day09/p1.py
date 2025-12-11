class Day9:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        self.tiles = []

        for line in lines:
            row, col = map(int, line.split(','))
            self.tiles.append((row, col))


    def solve(self):
        area = 0
        for a in self.tiles:
            for b in self.tiles:
                r1, c1 = a
                r2, c2 = b

                length = abs(r1 - r2) + 1
                height = abs(c1 - c2) + 1
                area = max(area, length * height)
        
        return area
    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day9(file.read())
    print(a.solve())