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


    def traverse(self, device):
        if device is None:
            return 0
        
        if device.token == 'out':
            return 1
        
        ways = 0
        for c in device.connections:
            next_device = self.find_device(c)
            ways += self.traverse(next_device)
        
        return ways

    def solve(self):
        you = self.find_device('svr')
        sum = self.traverse(you)
        return sum;    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day11(file.read())
    print(a.solve())