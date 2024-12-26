import itertools

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
                'in': [ wire_1, wire_2 ],
                'out': wire_out,
                'op': op
            })

    def find_output(self, in_1, in_2, op):
        for gate in self.gates:
            if in_1 in gate['in'] and in_2 in gate['in'] and gate['op'] == op:
                return gate
            
    def find_input(self, in_1, out, op):
        for gate in self.gates:
            if in_1 in gate['in'] and gate['out'] == out and gate['op'] == op:
                return gate
            
    def find_gate_by_input(self, in_1, op):
        for gate in self.gates:
            if in_1 in gate['in'] and gate['op'] == op:
                return gate
            
    def calculate(self):
        while len(self.gates) > 0:
            gate = self.gates.pop(0)

            if self.wires[gate['in'][0]] == -1 or self.wires[gate['in'][1]] == -1:
                self.gates.append(gate)
                continue

            if gate['op'] == 'OR':
                self.wires[gate['out']] = self.wires[gate['in'][0]] | self.wires[gate['in'][1]]
            elif gate['op'] == 'AND':
                self.wires[gate['out']] = self.wires[gate['in'][0]] & self.wires[gate['in'][1]]
            elif gate['op'] == 'XOR':
                self.wires[gate['out']] = self.wires[gate['in'][0]] ^ self.wires[gate['in'][1]]
            

    def solve(self):
        wires = []
        for key in self.wires.keys():
            if key == 'x00':
                continue
            if key.startswith('x'):
                wires.append(key)

        prev_carry = self.find_output('x00', 'y00', 'AND')

        wires.sort()

        wrong = set()
        for wire in wires:
            xin = wire
            yin = wire.replace('x', 'y')
            zout = wire.replace('x', 'z')
            
            int_xor = self.find_output(xin, yin, 'XOR')
            int_and = self.find_output(xin, yin, 'AND')

            int_xor_by_carry = self.find_gate_by_input(prev_carry['out'], 'XOR')
            int_and_by_carry = self.find_gate_by_input(prev_carry['out'], 'AND')

            other_input = list(filter(lambda x: x != prev_carry['out'], int_xor_by_carry['in']))[0]
            if int_xor['out'] != other_input:
                wrong.add((int_xor['out'], other_input))

            if (int_xor_by_carry['out'] != zout):
                wrong.add((int_xor_by_carry['out'], zout))

            prev_carry = self.find_gate_by_input(self.val_or_swap(wrong, int_and['out']), 'OR')
            prev_carry['out'] = self.val_or_swap(wrong, prev_carry['out'])

            

        
        print(wrong)
        self.parse(self.input)
        expected_val = self.calc_value('x') + self.calc_value('y')
        for t in wrong:
            gate_a = self.find_gate(t[0])
            gate_b = self.find_gate(t[1])

            gate_a['out'], gate_b['out'] = gate_b['out'], gate_a['out']


        self.calculate()
        if self.calc_value('z') == expected_val:
            print('hooray')
        
        wrong_list = []

        for t in wrong:
            wrong_list.append(t[0])
            wrong_list.append(t[1])

        wrong_list.sort()

        return ','.join(wrong_list)
            
    def val_or_swap(self, set, word):
        for tuple in set:
            if word in tuple:
                if tuple[0] == word:
                    return tuple[1]
                else:
                    return tuple[0]
        
        return word
    
    def find_gate(self, out):
        for gate in self.gates:
            if gate['out'] == out:
                return gate
    
    def calc_value(self, startswith):
        wires = []
        for key in self.wires.keys():
            if key.startswith(startswith):
                wires.append(key)
        
        wires.sort(reverse=True)


        result = 0
        for z_wire in wires:
            result = result << 1
            result = result + self.wires[z_wire]

        return result


if __name__ == '__main__':
    file = open('input', 'r')
    a = Day24(file.read())
    print(a.solve())