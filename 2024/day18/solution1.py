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


    def solve(self, n):
        for i in range(n):
            x, y = self.coordinates[i]
            self.grid[y][x] = '#'
        self.init_graph()

        print(self)

        nodes_left = []
        for node in self.nodes:
            nodes_left.append(node)
        
        while len(nodes_left) > 0:
            nodes_left.sort(key=lambda x: x.distance, reverse=True)
            curr_node = nodes_left.pop()

            for edge in curr_node.edges:
                neighbor = edge.node

                if curr_node.distance + edge.weight < neighbor.distance:
                    neighbor.distance = curr_node.distance + edge.weight
                    neighbor.prev = curr_node
        
        self.backtrack(self.end)

        return self.end.distance
    
    def backtrack(self, node):
        if node is None:
            return
        
        self.grid[node.row][node.col] = 'O'

        self.backtrack(node.prev)

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
    print(a.solve(1024))
    print(a)