import re

cache = {}

def parse_button(button):
    indicies = list(map(int, button.replace('(', '').replace(')', '').split(',')))
    indicies.sort(reverse=True)

    high = indicies[0]

    result = 0
    for i in range(high, -1, -1):
        result = result << 1
        if i in indicies:
            result += 1

    return result


class Machine:
    def __init__(self, buttons, joltages):
        self.buttons = buttons
        self.joltages = joltages

class Day10:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')

        self.machines = []

        for line in lines:
            matches = re.findall(r'\(\d+(?:,\d+)*\)', line)
            buttons = []
            for match in matches:
                button = list(map(int, match.replace('(', '').replace(')', '').split(',')))
                buttons.append(button)
            
            matches = re.findall(r'\{\d+(?:,\d+)*\}', line)
            joltages = list(map(int, matches[0].replace('{', '').replace('}', '').split(',')))

            self.machines.append(Machine(buttons, joltages))

    def press_button(self, state, button):
        new_state = state.copy()
        
        for index in button:
            new_state[index] -= 1

        return new_state
    
    def all_zeros(self, a):
        for x in a:
            if x != 0:
                return False
        return True
    
    def any_negative(self, a):
        for x in a:
            if x < 0:
                return True
        return False


    def press_buttons(self, current, buttons):
        key = f'{','.join(map(str, current))}-{','.join(map(str, buttons))}'

        if key in cache:
            return cache[key]

        if self.all_zeros(current):
            print('found solution')
            return 0
        
        if self.any_negative(current):
            return float('inf')
        
        result = float('inf')
        for button in buttons:
            new_current = self.press_button(current, button)
            print(current, button, new_current)

            num_clicks = 1 + self.press_buttons(new_current, buttons)

            result = min([num_clicks, result])

        cache[key] = result

        return result

    def solve(self):
        sum = 0

        for machine in self.machines:
            clicks = self.press_buttons(machine.joltages, machine.buttons)
            print(clicks)
            sum += clicks

        return sum;    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day10(file.read())
    print(a.solve())