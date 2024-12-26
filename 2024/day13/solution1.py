import re

class Game:
    def __init__(self, button_a, button_b, prize):
        self.a = button_a
        self.b = button_b
        self.prize = prize

    def solve(self):
        solves = []

        for i in range(100):
            for j in range(100):
                x = self.a[0] * i + self.b[0] * j
                y = self.a[1] * i + self.b[1] * j

                if x == self.prize[0] and y == self.prize[1]:
                    solves.append(i * 3 + j)

        solves.sort()

        if len(solves) > 0:
            return solves[0]
        return 0

class Day13:
    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.games = []

        for game in input.split('\n\n'):
            lines = game.split('\n')
            a_x = int(re.findall('X\+\d+', lines[0])[0].split('+')[1])
            a_y = int(re.findall('Y\+\d+', lines[0])[0].split('+')[1])
            b_x = int(re.findall('X\+\d+', lines[1])[0].split('+')[1])
            b_y = int(re.findall('Y\+\d+', lines[1])[0].split('+')[1])
            prize_x = int(re.findall('X\=\d+', lines[2])[0].split('=')[1])
            prize_y = int(re.findall('Y\=\d+', lines[2])[0].split('=')[1])

            self.games.append(Game((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))

    def solve(self):
        sum = 0
        num_won = 0

        for game in self.games:
            score = game.solve()
            if score > 0:
                num_won = num_won + 1
            sum = sum + score
        
        print(num_won)
        return sum

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day13(file.read())
    print(a.solve())