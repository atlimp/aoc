import re

cache = {}

def parse_light(light):
    result = 0
    for i in range(len(light) - 1, -1, -1):
        result = result << 1
        token = light[i]
        if token == '#':
            result += 1
    
    return result

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
    def __init__(self, target, buttons):
        self.target = target
        self.buttons = buttons

class Day10:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')

        self.machines = []

        for line in lines:
            match = re.match(r'\[[\.#]*\]', line)
            target_light = match.group().replace('[', '').replace(']', '')
            target = parse_light(target_light)
            matches = re.findall(r'\(\d+(?:,\d+)*\)', line)

            buttons = []
            for match in matches:
                button = parse_button(match)
                buttons.append(button)

            self.machines.append(Machine(target, buttons))

    def press_buttons(self, target, current, buttons):
        key = f'{target}-{current}-{','.join(map(str, buttons))}'

        if key in cache:
            return cache[key]

        if target == current:
            return 0
        
        if len(buttons) <= 0:
            return float('inf')
        
        result = float('inf')
        for i in range(len(buttons)):
            rest = buttons.copy()
            selected = rest.pop(i)
            new_current = current ^ selected

            num_clicks = 1 + self.press_buttons(target, new_current, rest)

            result = min([num_clicks, result])

        cache[key] = result

        return result

    def solve(self):
        sum = 0
        for machine in self.machines:
            clicks = self.press_buttons(machine.target, 0, machine.buttons)
            sum += clicks

        return sum;    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day10(file.read())
    print(a.solve())