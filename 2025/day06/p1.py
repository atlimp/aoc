import re

class Homework:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')
        
        self.problems = []
        
        for line in lines:
            numbers = list(filter(lambda x: x != '', re.split(r"\s+", line)))
            if len(self.problems) == 0:
                self.problems = [[] for _ in range(len(numbers))]

            for i in range(len(numbers)):
                self.problems[i].append(numbers[i])            


    def solve(self):
        sum = 0
        for problem in self.problems:
            operand = problem.pop()
            answer = 0
            if operand == '*':
                answer = 1
            for num in map(int, problem):
                if operand == '+':
                    answer += num
                elif operand == '*':
                    answer *= num
            print(answer)
            sum += answer
        return sum



if __name__ == '__main__':
    file = open('input', 'r')
    a = Homework(file.read())
    print(a.solve())