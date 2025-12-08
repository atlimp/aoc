class JunctionBox:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.connections = []
        self.visited = False

    def distance(self, other):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates

        return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    
    def connect(self, other):
        if not other in self.connections:
            self.connections.append(other)
        if not self in other.connections:
            other.connections.append(self)
    
    def __str__(self):
        x, y, z = self.coordinates
        return f'({x}, {y}, {z})'

class Day7:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        
        self.junction_boxes = []
        for line in lines:
            x, y, z = map(int, line.split(','))
            self.junction_boxes.append(JunctionBox((x, y, z)))

        distances = {}
        for i in range(len(self.junction_boxes)):
            for j in range(len(self.junction_boxes)):
                if i == j: continue
                indicies = [i, j]
                indicies.sort()
                key = ','.join(map(lambda x: f'{x}', indicies))
                if not key in distances:
                    a = self.junction_boxes[i]
                    b = self.junction_boxes[j]
                    distances[key] = a.distance(b)
        
        self.distances = []
        for key in distances.keys():
            self.distances.append((key, distances[key]))

    def circuit_size(self, box):
        box.visited = True

        result = 1
        for other in box.connections:
            if not other.visited:
                result += self.circuit_size(other)

        return result
    
    def is_connected(self):
        size = self.circuit_size(self.junction_boxes[0])
        length = len(self.junction_boxes)
        print(f'[{size}/{length}]')

        for box in self.junction_boxes:
            box.visited = False

        return size == length

    def solve(self):
        self.distances.sort(key= lambda x: x[1])
        print(len(self.distances))
        for i in range(len(self.distances)):
            indicies, _ = self.distances[i]
            i_a, i_b = map(int, indicies.split(','))
            box_a = self.junction_boxes[i_a]
            box_b = self.junction_boxes[i_b]
            box_a.connect(box_b)

            if self.is_connected():
                a_x, _, _ = box_a.coordinates
                b_x, _, _ = box_b.coordinates
                return a_x * b_x

        return 0


    
    def print(self):
        for box in self.junction_boxes:
            print(box)

if __name__ == '__main__':
    #file = open("C:\\Users\\AtliMarcherPálsson\\source\\repos\\aoc\\2025\\day08\\input", 'r')
    file = open('input', 'r')
    a = Day7(file.read())
    print(a.solve())