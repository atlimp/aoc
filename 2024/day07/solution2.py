class Equation:

    def __init__(self, input):
        self.input = input
        split = input.split(':')
        self.solution = int(split[0])
        self.numbers = list(map(int, split[1].strip().split(' ')))
        self.operators = ['+', '*', '|']

    def get_operators(self, n, length):
        if n == 0:
            return ['+'] * length
        nums = []
        while n:
            n, r = divmod(n, len(self.operators))
            nums.append(self.operators[r])
        
        while (len(nums) < length):
            nums.append(self.operators[0])

        return nums[::-1]

    def has_solution(self):
        print(self)
        operator_len = len(self.numbers) - 1
        num_loops = (len(self.operators) ** operator_len)
        print('Number of loops: ', num_loops)
        for i in range(0, num_loops):
            operators = self.get_operators(i, operator_len)
            calculation = self.calculate(operators)
            if calculation == self.solution:
                print(self.solution, operators)
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
            elif token == '|':
                result = int(f'{result}{num}')
        
        return result
    
    def __str__(self):
        return self.input


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
    #a = BridgeCalibration('161011: 16 10 13 12')
    print(a.solve())