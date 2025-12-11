import re

cache = {}

class Device:
    def __init__(self, token, connections):
        self.token = token
        self.connections = connections

class Day11:
    def __init__(self, input):
        self.parse(input)
    
    def parse(self, input):
        lines = input.split('\n')

        self.devices = []

        for line in lines:
            split = line.split(': ')

            device, connection_str = split
            connections = connection_str.split(' ')

            self.devices.append(Device(device, connections))
        self.devices.append(Device('out', []))

    def find_device(self, device_token):
        for device in self.devices:
            if device.token == device_token:
                return device


    def traverse(self, prev, curr, path):
        key = f'{prev.token}-{curr.token}'

        if key in cache:
            print(key)
            return cache[key]
        
        if curr is None:
            return 0
        
        if curr.token == 'out':
            print(path)
            if 'fft' in path and 'dac' in path:
                print(path)
                return 1
            return 0
        
        ways = 0
        for c in curr.connections:
            if c in path: # looping
                continue


            next_device = self.find_device(c)
            if curr.token == 'svr':
                print(path, next_device.token)
            new_path = path.copy()
            new_path.append(c)
            ways += self.traverse(curr, next_device, new_path)

        cache[key] = ways
        
        return ways

    def solve(self):
        you = self.find_device('svr')
        sum = self.traverse(Device('', []), you, ['svr'])
        return sum;    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day11(file.read())
    print(a.solve())