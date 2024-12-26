import itertools

class Graph:
    def __init__(self):
        self.dict = {}

    def add_edge(self, a, b):
        if a not in self.dict:
            self.dict[a] = []

        if b not in self.dict:
            self.dict[b] = []

        self.dict[a].append(b)
        self.dict[b].append(a)

    def is_clique(self, clique):
        for a in clique:
            for b in clique:
                if a == b:
                    continue

                if a not in self.dict[b]:
                    return False
            
        return True

    def find_cliques(self, size):
        keys = self.dict.keys()

        cliques = []
        possible_cliques = itertools.combinations(keys, size)
        for candidate in possible_cliques:
            if self.is_clique(candidate):
                cliques.append(candidate)
        
        return cliques


class Day23:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        self.graph = Graph()
        for line in input.split('\n'):
            a, b = line.split('-')
            self.graph.add_edge(a, b)

    def solve(self, clique_size, starts_with):
        cliques = self.graph.find_cliques(clique_size)
        
        starts_with_cliques = set()
        for clique in cliques:
            for node in clique:
                if node.startswith(starts_with):
                    starts_with_cliques.add(clique)
                    continue
                
        return len(starts_with_cliques)

        

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day23(file.read())
    print(a.solve(3, 't'))