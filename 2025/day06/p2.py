import re

class Homework:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        operand_line = lines.pop()
        operands = []

        for i in range(len(operand_line)):
            token = operand_line[i]
            if token != ' ':
                operands.append((token, i))

        self.problems = [[] for _ in range(len(operands))]
        for line in lines:
            for i in range(len(operands) - 1):
                _, i1 = operands[i]
                _, i2 = operands[i + 1]
                number = line[i1:i2 - 1]
                self.problems[i].append(number)
            
            _, i_last = operands[-1]
            number = line[i_last:]
            self.problems[-1].append(number)

        for i in range(len(operands)):
            t, _ = operands[i]
            self.problems[i].append(t)
        
        print(self.problems)

    def solve(self):
        sum = 0
        for problem in self.problems:
            operand = problem.pop()

            answer = 0
            if operand == '*':
                answer = 1

            for i in range(len(problem[0]) -1, -1, -1):
                number = ''
                for numbers in problem:
                    number += numbers[i]

                if operand == '*':
                    answer *= int(number)
                elif operand == '+':
                    answer += int(number)
            
            sum += answer

        return sum



if __name__ == '__main__':
    file = open('input', 'r')
    a = Homework(file.read())
    print(a.solve())