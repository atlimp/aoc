cache = {}

class Day19:
    def __init__(self, input):
        self.input = input
        self.parse(input)

    def parse(self, input):
        split = input.split('\n\n')

        self.patterns = split[0].split(', ')

        self.towels = split[1].split('\n')

        self.top_level_patterns = {}
        for towel in self.patterns:
            sum = 0
            todo = [(towel, [])]

            top_level_key = ''

            while len(todo) > 0:
                to_check, current_list = todo.pop()

                if len(to_check) <= 0:
                    sum = sum + 1
                    if len(current_list) == 1:
                        top_level_key = current_list[0]

                for pattern in self.patterns:
                    if to_check.startswith(pattern):
                        todo.append((to_check[len(pattern):], current_list + [pattern]))

            if top_level_key != '':
                self.top_level_patterns[top_level_key] = sum
            
            self.patterns.sort(key=lambda x: len(x), reverse=True)

    def match_word(self, word, list):
        global cache

        if word in cache:
            return cache[word]
        
        if len(word) <= 0:
            return 1
        
        result = 0
        for pattern in self.patterns:
            if word.startswith(pattern):
                result = result + self.match_word(word[len(pattern):], list + [pattern])

        cache[word] = result

        return result

                

    def solve(self):
        cache = {}
        sum = 0
        for i in range(len(self.towels)):
            print(f'[{i}/{len(self.towels)}]')
            sum = sum + self.match_word(self.towels[i], [])
        
        return sum


if __name__ == '__main__':
    file = open('input', 'r')
    a = Day19(file.read())
    print(a.top_level_patterns)
    print(a.solve())