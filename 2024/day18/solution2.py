class Node:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.edges = []
        self.prev = None
        self.distance = float('inf')

class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

class Maze:
    def __init__(self, input, height, width):
        self.input = input
        self.nodes = []
        self.height = height
        self.width = width
        self.parse(input, height, width)

    def find_or_create_node(self, row, col):
        for node in self.nodes:
            if (node.row == row and node.col == col):
                return node
            
        node = Node(row, col, dir)
        self.nodes.append(node)
        return node
    
    def parse(self, input, height, width):
        self.coordinates = []

        for c in input.split('\n'):
            x, y = list(map(int, c.split(',')))
            self.coordinates.append((x, y))

        self.grid = []
        
        for row in range(height):
            self.grid.append([])
            for col in range(width):
                self.grid[row].append('.')

    def init_graph(self):
        self.nodes = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                token = self.grid[row][col]

                if (token == '#'):
                    continue

                node = self.find_or_create_node(row, col)

                if row == 0 and col == 0:
                    self.start = node
                    self.start.distance = 0


                if row == self.height - 1 and col == self.width - 1:
                    self.end = node

                # NORTH
                if row - 1 >= 0 and self.grid[row - 1][col] == '.':
                    node.edges.append(Edge(self.find_or_create_node(row - 1, col), 1))
                # EAST
                if col + 1 < len(self.grid[row]) and self.grid[row][col + 1] == '.':
                    node.edges.append(Edge(self.find_or_create_node(row, col + 1), 1))
                # SOUTH
                if row + 1 < len(self.grid) and self.grid[row + 1][col] == '.':
                    node.edges.append(Edge(self.find_or_create_node(row + 1, col), 1))
                # WEST
                if col - 1 >= 0 and self.grid[row][col - 1] == '.':
                    node.edges.append(Edge(self.find_or_create_node(row, col - 1), 1))

    def is_reachable(self):
        nodes_left = self.nodes.copy()

        while len(nodes_left) > 0:
            nodes_left.sort(key=lambda x: x.distance, reverse=True)
            curr_node = nodes_left.pop()

            for edge in curr_node.edges:
                neighbor = edge.node

                if curr_node.distance + edge.weight < neighbor.distance:
                    neighbor.distance = curr_node.distance + edge.weight
                    neighbor.prev = curr_node

        prev = self.end
        self.path = []
        while prev is not None:
            self.path.append((prev.row, prev.col))
            prev = prev.prev

        return not self.end.prev is None

    def is_in_path(self, x, y):
        for c in self.path:
            row, col = c
            if row == y and col == x:
                return True
        
        return False

    def solve(self):
        self.init_graph()
        self.is_reachable()

        for n in range(len(self.coordinates)):
            print(n)
            x, y = self.coordinates[n]
            self.grid[y][x] = '#'

            if (self.is_in_path(x, y)):
                self.init_graph()

                if not self.is_reachable():
                    return (y, x)
        
        return None

    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s = s + col
            
            s = s + '\n'
        
        return s

if __name__ == '__main__':
    file = open('input', 'r')
    a = Maze(file.read(), 71, 71)
    print(a)
    print(a.solve())
    print(a)