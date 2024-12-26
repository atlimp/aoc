def taxicab_distance(node_a, node_b):
    return abs(node_a.row - node_b.row) + abs(node_a.col - node_b.col)

class Node:
    def __init__(self, row, col, token):
        self.row = row
        self.col = col
        self.token = token
        self.visited = False
        self.prev = None
        self.distance = float('inf')

class Maze: 
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        self.grid = []

        row = 0
        for line in input.split('\n'):
            self.grid.append([])
            col = 0
            for token in list(line):
                node = Node(row, col, token)
                self.grid[row].append(node)
                if token == 'S':
                    self.start = node
                col = col + 1
            row = row + 1

    def find_neighbors(self, node, dist):
        neighbors = []

        row = node.row
        col = node.col

        # NORTH
        if row - dist >= 0 and self.grid[row - dist][col].token != '#':
            neighbors.append(((-dist, 0), self.grid[row - dist][col]))
        # EAST
        if col + dist < len(self.grid[row]) and self.grid[row][col + dist].token != '#':
            neighbors.append(((0, dist), self.grid[row][col + dist]))
        # SOUTH
        if row + dist < len(self.grid) and self.grid[row + dist][col].token != '#':
            neighbors.append(((dist, 0), self.grid[row + dist][col]))
        # WEST
        if col - dist >= 0 and self.grid[row][col - dist].token != '#':
            neighbors.append(((0, -dist), self.grid[row][col - dist]))

        return neighbors

    def bfs(self):
        queue = []

        queue.append(self.start)
        self.start.visited = True
        self.start.distance = 0

        while len(queue) > 0:
            node = queue.pop(0)
            
            if (node.token == 'E'):
                self.end = node
                break
        
            for neighbor in self.find_neighbors(node, 1):
                offsets, neighbor_node = neighbor
                if not neighbor_node.visited:
                    neighbor_node.visited = True
                    neighbor_node.prev = node
                    neighbor_node.distance = node.distance + 1
                    queue.append(neighbor_node)

    def solve(self, cheat_secs, min_saved):
        self.bfs()
        path = []
        node = self.end
        while node is not None:
            path.append(node)
            node = node.prev
        
        path = path[::-1]

        cheats = {}
        for node in path:
            for other_node in path:
                if node == other_node:
                    continue

                taxi_dist = taxicab_distance(node, other_node)

                if taxi_dist > cheat_secs:
                    continue

                distance_from_end = self.end.distance - other_node.distance
                distance_gone = node.distance

                distance_saved = self.end.distance - (distance_gone + distance_from_end + taxi_dist)

                if distance_saved > 0:
                    if distance_saved not in cheats:
                        cheats[distance_saved] = 0
                    cheats[distance_saved] = cheats[distance_saved] + 1

        
        sum = 0
        for key in cheats.keys():
            if int(key) >= min_saved:
                sum = sum + cheats[key]
        
        return sum



    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s = s + col.token
            
            s = s + '\n'
        
        return s
    
if __name__ == '__main__':
    file = open('input', 'r')
    a = Maze(file.read())
    #print(a)
    print(a.solve(20, 100))