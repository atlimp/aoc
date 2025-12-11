class Day9:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        self.tiles = []

        for line in lines:
            col, row = map(int, line.split(','))
            self.tiles.append((row, col))


    def hasTile(self, f):
        try:
            next(i for i,v in enumerate(self.tiles) if f(v))
            return True
        except:
            return False
        
    def pair_is_valid(self, tile_1, tile_2):
        row_a, col_a = tile_1
        row_b, col_b = tile_2

        d_row = abs(row_b - row_a)
        d_col = abs(col_b - col_a)

        corner_a = (min([row_a, row_b]), min([col_a, col_b]))
        corner_b = (corner_a[0], corner_a[1] + d_col)
        corner_c = (corner_b[0] + d_row, corner_b[1])
        corner_d = (corner_c[0], corner_c[1] - d_col)

        if self.hasTile(lambda x: x[0] > corner_a[0] and x[0] < corner_d[0] and x[1] > corner_a[1] and x[1] < corner_b[1]):
            return False
        
        if not self.hasTile(lambda x: x[0] <= corner_a[0] and x[1] <= corner_a[1]):
            return False
        if not self.hasTile(lambda x: x[0] <= corner_b[0] and x[1] >= corner_b[1]):
            return False
        if not self.hasTile(lambda x: x[0] >= corner_c[0] and x[1] >= corner_c[1]):
            return False
        if not self.hasTile(lambda x: x[0] >= corner_d[0] and x[1] <= corner_d[1]):
            return False
        
        if corner_a[0] <= 48563 and corner_d[0] >= 50218 and corner_a[1] >= 2402 and corner_b[1] <= 94880: #magic numbers!
            return False


        return True

    def solve(self):
        max_area = 0
        for i in range(len(self.tiles)):
            for j in range(i + 1, len(self.tiles)):

                tile_a = self.tiles[i]
                tile_b = self.tiles[j]

                if self.pair_is_valid(tile_a, tile_b):
                    area = (abs(tile_a[0] - tile_b[0]) + 1) * (abs(tile_a[1] - tile_b[1]) + 1)
                    if area > max_area:
                        print(f'checking pair [{i}] and [{j}]')
                        print(f'Found new max area {area}')
                        max_area = area

        return max_area

if __name__ == '__main__':
    file = open('input', 'r')
    #file = open("2025\day09\input", 'r')
    a = Day9(file.read())
    print(a.solve())