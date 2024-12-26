from itertools import combinations

class Equation:

    def __init__(self, input):
        split = input.split(':')
        self.solution = int(split[0])
        self.numbers = list(map(int, split[1].strip().split(' ')))

    def has_solution(self):

        for i in range(0, len(self.numbers)):
            multipliers = list(range(len(self.numbers) - 1))

            mult_positions = combinations(multipliers, i)

            for perm in mult_positions:
                operators = ['+'] * (len(self.numbers) - 1)
                for pos in perm:
                    operators[pos] = '*'
                
                if self.calculate(operators) == self.solution:
                    return True
            
        return False

    def calculate(self, operators):
        result = self.numbers[0]
        for i in range(1, len(self.numbers)):
            token = operators[i - 1]
            num = self.numbers[i]

            if token == '+':
                result = result + num
            elif token == '*':
                result = result * num
        
        return result


class BridgeCalibration:

    def __init__(self, input):
        self.equations = []
        self.parse(input)

    def parse(self, input):
        for line in input.split('\n'):
            self.equations.append(Equation(line))

    def solve(self):
        sum = 0
        for equation in self.equations:
            if equation.has_solution():
                sum = sum + equation.solution
        
        return sum
    


if __name__ == "__main__":
    file = open('input', 'r')
    a = BridgeCalibration(file.read())
    print(a.solve())