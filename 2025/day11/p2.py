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


    def traverse(self, curr, end):
        key = f'{curr}-{end}'

        if key in cache:
            return cache[key]
        
        if curr is None:
            return 0
        
        if curr.token == end:
            return 1
        
        ways = 0
        for c in curr.connections:
            next_device = self.find_device(c)
            ways += self.traverse(next_device, end)

        cache[key] = ways
        
        return ways

    def solve(self):
        svr = self.find_device('svr')
        fft = self.find_device('fft')
        dac = self.find_device('dac')

        svr_dac = self.traverse(svr, 'dac')
        svr_fft = self.traverse(svr, 'fft')
        dac_fft = self.traverse(dac, 'fft')
        fft_dac = self.traverse(fft, 'dac')
        dac_out = self.traverse(dac, 'out')
        fft_out = self.traverse(fft, 'out')

        print('svr_dac', svr_dac)
        print('svr_fft', svr_fft)
        print('dac_fft', dac_fft)
        print('fft_dac', fft_dac)
        print('dac_out', dac_out)
        print('fft_out', fft_out)

        via_dac_fft = svr_dac
        via_dac_fft *= dac_fft
        via_dac_fft *= fft_out

        via_fft_dac = svr_fft
        via_fft_dac *= fft_dac
        via_fft_dac *= dac_out

        return via_dac_fft + via_fft_dac;    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day11(file.read())
    print(a.solve())