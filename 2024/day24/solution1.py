class Day24:
    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        initial_values, gates = input.split('\n\n')

        self.wires = {}
        for line in initial_values.split('\n'):
            wire, value = line.split(': ')
            
            if wire not in self.wires:
                self.wires[wire] = int(value)

        self.gates = []

        for gate in gates.split('\n'):
            wire_1, op, wire_2, _, wire_out = gate.split(' ')
            
            if wire_1 not in self.wires:
                self.wires[wire_1] = -1
            if wire_2 not in self.wires:
                self.wires[wire_2] = -1
            if wire_out not in self.wires:
                self.wires[wire_out] = -1

            self.gates.append({
                'in_1': wire_1,
                'in_2': wire_2,
                'out': wire_out,
                'op': op
            })

    def solve(self):
        
        while len(self.gates) > 0:
            gate = self.gates.pop(0)

            if self.wires[gate['in_1']] == -1 or self.wires[gate['in_2']] == -1:
                self.gates.append(gate)
                continue

            if gate['op'] == 'OR':
                self.wires[gate['out']] = self.wires[gate['in_1']] | self.wires[gate['in_2']]
            elif gate['op'] == 'AND':
                self.wires[gate['out']] = self.wires[gate['in_1']] & self.wires[gate['in_2']]
            elif gate['op'] == 'XOR':
                self.wires[gate['out']] = self.wires[gate['in_1']] ^ self.wires[gate['in_2']]

        z_wires = []
        for key in self.wires.keys():
            if key.startswith('z'):
                z_wires.append(key)
        
        z_wires.sort(reverse=True)


        result = 0
        for z_wire in z_wires:
            result = result << 1
            result = result + self.wires[z_wire]

        return result


if __name__ == '__main__':
    file = open('input', 'r')
    a = Day24(file.read())
    print(a.solve())