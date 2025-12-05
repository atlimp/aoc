class Ingredients:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        
        self.ranges = []
        self.ids = []
        
        checking_ranges = True
        for line in lines:
            if line == '':
                checking_ranges = False
                continue

            if checking_ranges:
                min, max = map(int, line.split('-'))
                self.ranges.append((min, max))
            else:
                self.ids.append(int(line))

    def within_range(self, id):
        for id_range in self.ranges:
            min, max = id_range
            if id >= min and id <= max:
                return True
        
        return False

    def solve(self):
        count = 0
        for id in self.ids:
            if self.within_range(id):
                count += 1
        
        return count



if __name__ == '__main__':
    file = open('input', 'r')
    a = Ingredients(file.read())
    print(a.solve())