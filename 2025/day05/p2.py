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

    def overlaps(self, min_a, max_a, min_b, max_b):
        if min_a >= min_b and min_a <= max_b:
            return True
        if min_b >= min_a and min_b <= max_a:
            return True
                 

    def merge_ranges(self):

        candidates = self.ranges.copy()
        has_merge = True
        while has_merge:
            new_candidates = []
            has_merge = False

            while len(candidates) > 0:
                range_a = candidates.pop()

                for i in range(len(candidates) - 1, -1, -1):
                    range_b = candidates[i]
                    min_a, max_a = range_a
                    min_b, max_b = range_b

                    if self.overlaps(min_a, max_a, min_b, max_b):
                        has_merge = True
                        range_a = (min(min_a, min_b), max(max_a, max_b))
                        candidates.remove(range_b)

                new_candidates.append(range_a)
            
            candidates = new_candidates.copy()
        
        self.ranges = candidates




    def solve(self):
        self.merge_ranges()

        fresh_count = 0
        for min, max in self.ranges:
            fresh_count += (max - min) + 1

        
        return fresh_count



if __name__ == '__main__':
    #file = open("C:\\Users\\AtliMarcherPálsson\\source\\repos\\aoc\\2025\\day05\\input", 'r')
    file = open('input', 'r')
    a = Ingredients(file.read())
    print(a.solve())