cache = {}

class Stone:
    def __init__(self, data):
        self.data = data

    def blink(self, n):
        global cache
        key = f'{self.data},{n}'

        if key in cache:
            return cache[key]
        
        if n == 0:
            return 1

        result = 0
        if self.data == 0:
            self.data = 1
            result = self.blink(n - 1)
        elif len(f'{self.data}') % 2 == 0:
            string_data = f'{self.data}'
            len_data = len(string_data)
            a = int(string_data[0:(len_data//2)])
            b = int(string_data[len_data//2:len_data])
            result = Stone(a).blink(n - 1) + Stone(b).blink(n - 1)
        else:
            self.data = self.data * 2024
            result = self.blink(n - 1)

        cache[key] = result

        return result

class Line:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        self.stones = list(map(Stone, list(map(int, input.split(' ')))))

    def solve(self, n):
        
        count = 0
        for i in range(len(self.stones)):
            print(f'[{i}/{len(self.stones)}]')
            count = count + self.stones[i].blink(n)

        return count
    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Line(file.read())
    print(a.solve(75))