class Day25:
    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.locks = []
        self.keys = []

        for schematic in input.split('\n\n'):
            lines = schematic.split('\n')
            if lines[0] == '#####':  #Lock
                lock = [0, 0, 0, 0, 0]
                for i in range(1, len(lines)):
                    line = lines[i]
                    for j in range(len(line)):
                        c = line[j]
                        if c == '#':
                            lock[j] = lock[j] + 1
                self.locks.append(lock)
            else:
                key = [0, 0, 0, 0, 0]
                for i in range(len(lines) - 2, 0, -1):
                    line = lines[i]
                    for j in range(len(line)):
                        c = line[j]
                        if c == '#':
                            key[j] = key[j] + 1
                self.keys.append(key)

    def solve(self):
        matches = 0
        for key in self.keys:
            for lock in self.locks:
                if not self.overlaps(key, lock):
                    matches = matches + 1
        
        return matches
    

    def overlaps(self, key, lock):
        for i in range(len(key)):
            key_pin = key[i]
            lock_pin = lock[i]
            if key_pin + lock_pin > 5:
                return True
        
        return False
                



if __name__ == '__main__':
    file = open('input', 'r')
    a = Day25(file.read())
    print(a.solve())