class Plot:
    def __init__(self, token):
        self.token = token
        self.visited = False


class Region:
    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.grid = []

        for line in input.split('\n'):
            self.grid.append(list(map(Plot, list(line))))

    def solve(self):
        total_price = 0

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                plot = self.grid[row][col]

                if not plot.visited:
                    area, perimeter = self.fill_region(plot, row, col)
                    print(f'Region {plot.token}: Area = {area}, Perimeter = {perimeter}')
                    total_price = total_price + area * perimeter

        return total_price

        
    def fill_region(self, plot, row, col):
        plot.visited = True
        neighbors = self.find_neighbors(plot, row, col)

        area = 1
        perimeter = 4 - len(neighbors)

        for neighbor in neighbors:
            neighbor_plot = self.grid[neighbor[0]][neighbor[1]]

            if neighbor_plot.visited:
                continue

            a, p = self.fill_region(neighbor_plot, neighbor[0], neighbor[1])
            area = area + a
            perimeter = perimeter + p

        return (area, perimeter)


    def find_neighbors(self, plot, row, col):
        neighbors = []

        if not (row >= 0 and row < len(self.grid) and col >= 0 and col < len(self.grid[0])):
            return neighbors

        # NORTH
        if (row - 1) >= 0 and (row - 1) < len(self.grid):
            if self.grid[row - 1][col].token == plot.token:
                neighbors.append((row - 1, col))

        # EAST
        if (col + 1) >= 0 and (col + 1) < len(self.grid):
            if self.grid[row][col + 1].token == plot.token:
                neighbors.append((row, col + 1))

        # SOUTH
        if (row + 1) >= 0 and (row + 1) < len(self.grid):
            if self.grid[row + 1][col].token == plot.token:
                neighbors.append((row + 1, col))
        
        # WEST
        if (col - 1) >= 0 and (col - 1) < len(self.grid):
            if self.grid[row][col - 1].token == plot.token:
                neighbors.append((row, col - 1))

        return neighbors

if __name__ == '__main__':
    file = open('input', 'r')
    a = Region(file.read())
    print(a.solve())