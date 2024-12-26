NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Node:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.edges = []
        self.prev = None
        self.distance = float('inf')

class Edge:
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

class Maze:
    def __init__(self, input):
        self.input = input
        self.nodes = []
        self.parse(input)

    def find_or_create_node(self, row, col, dir):
        for node in self.nodes:
            if (node.row == row and node.col == col and node.direction == dir):
                return node
            
        node = Node(row, col, dir)
        self.nodes.append(node)
        return node

    def parse(self, input):
        self.grid = []

        for line in input.split('\n'):
            self.grid.append(list(line))

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 'S':
                    self.start = Node(row, col, EAST)
                    self.start.distance = 0
                    self.nodes.append(self.start)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                token = self.grid[row][col]
                if token != '#':
                    north_node = self.find_or_create_node(row, col, NORTH)
                    east_node = self.find_or_create_node(row, col, EAST)
                    south_node = self.find_or_create_node(row, col, SOUTH)
                    west_node = self.find_or_create_node(row, col, WEST)

                    if self.grid[row - 1][col] != '#':
                        north_node.edges.append(Edge(self.find_or_create_node(row - 1, col, NORTH), 1))
                    if self.grid[row][col + 1] != '#':
                        east_node.edges.append(Edge(self.find_or_create_node(row, col + 1, EAST), 1))
                    if self.grid[row + 1][col] != '#':
                        south_node.edges.append(Edge(self.find_or_create_node(row + 1, col, SOUTH), 1))
                    if self.grid[row][col] != '#':
                        west_node.edges.append(Edge(self.find_or_create_node(row, col - 1, WEST), 1))

                    if (token == 'E'):
                        self.end = north_node
                        north_node.edges.append(Edge(east_node, 0))
                        north_node.edges.append(Edge(west_node, 0))

                        east_node.edges.append(Edge(north_node, 0))
                        east_node.edges.append(Edge(south_node, 0))

                        south_node.edges.append(Edge(east_node, 0))
                        south_node.edges.append(Edge(west_node, 0))

                        west_node.edges.append(Edge(north_node, 0))
                        west_node.edges.append(Edge(south_node, 0))
                    else:
                        north_node.edges.append(Edge(east_node, 1000))
                        north_node.edges.append(Edge(west_node, 1000))

                        east_node.edges.append(Edge(north_node, 1000))
                        east_node.edges.append(Edge(south_node, 1000))

                        south_node.edges.append(Edge(east_node, 1000))
                        south_node.edges.append(Edge(west_node, 1000))

                        west_node.edges.append(Edge(north_node, 1000))
                        west_node.edges.append(Edge(south_node, 1000))  
                
    def solve(self):
        
        nodes_left = []
        for node in self.nodes:
            nodes_left.append(node)
        
        while len(nodes_left) > 0:
            print(f'Nodes left: {len(nodes_left)}')
            nodes_left.sort(key=lambda x: x.distance, reverse=True)
            curr_node = nodes_left.pop()

            if (curr_node == self.end):
                return self.end.distance

            for edge in curr_node.edges:
                neighbor = edge.node

                if curr_node.distance + edge.weight < neighbor.distance:
                    neighbor.distance = curr_node.distance + edge.weight
                    neighbor.prev = curr_node
        
        
        return self.end.distance

        
    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s = s + col
            
            s = s + '\n'
        
        return s

if __name__ == '__main__':
    file = open('input', 'r')
    a = Maze(file.read())
    print(a)
    print(a.solve())
