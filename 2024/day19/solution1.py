
class Day19:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        split = input.split('\n\n')

        self.patterns = split[0].split(', ')

        self.towels = split[1].split('\n')

    def solve(self):

        sum = 0
        for towel in self.towels:

            todo = [(towel, [])]

            while len(todo) > 0:
                to_check, current_list = todo.pop()

                if len(to_check) <= 0:
                    print(current_list)
                    sum = sum + 1
                    break

                for pattern in self.patterns:
                    if to_check.startswith(pattern):
                        todo.append((to_check[len(pattern):], current_list + [pattern]))
        
        return sum


if __name__ == '__main__':
    file = open('input', 'r')
    a = Day19(file.read())
    print(a.solve())