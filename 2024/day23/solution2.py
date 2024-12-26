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
        possible_len = sum(1 for _ in possible_cliques)
        possible_cliques = itertools.combinations(keys, size)
        i = 1
        for candidate in possible_cliques:
            print(f'{i}/{possible_len}')
            if self.is_clique(candidate):
                cliques.append(candidate)
            i = i + 1
        
        return cliques
    
    def maximal_clique(self):
        clique = list(self.BronKerbosch(None, set(self.dict.keys()), None))
        return clique

    def BronKerbosch(self, R, P, X):
        P = set(P)
        R = set() if R is None else R
        X = set() if X is None else X
        if not P and not X:
            yield R
        while P:
            v = P.pop()
            yield from self.BronKerbosch(
                P=P.intersection(set(self.dict[v])), R=R.union([v]), X=X.intersection(set(self.dict[v])))
            X.add(v)



class Day23:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        self.graph = Graph()
        for line in input.split('\n'):
            a, b = line.split('-')
            self.graph.add_edge(a, b)

    def solve(self):
        max_edges = map(lambda x: len(self.graph.dict[x]), self.graph.dict.keys())
        max_clique = None
        for i in range(max(max_edges), 0, -1):
            print(i)
            cliques = self.graph.find_cliques(i)
            if (len(cliques) > 0):
                max_clique = cliques[0]
                break
        
        max_clique.sort()
        return ','.join(max_clique)



        

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day23(file.read())
    print(a.solve())