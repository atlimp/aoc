def compare(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
        
    return True

class Computer:
    def __init__(self, input):
        self.input = input
        self.parse(input)
        

    def parse(self, input):
        self.ir = 0
        self.output = []
        for line in input.split('\n'):
            if line.startswith('Register A: '):
                value = line.replace('Register A: ', '')
                self.reg_a = int(value)
                
            elif line.startswith('Register B: '):
                value = line.replace('Register B: ', '')
                self.reg_b = int(value)
            
            elif line.startswith('Register C: '):
                value = line.replace('Register C: ', '')
                self.reg_c = int(value)

            elif line.startswith('Program: '):
                value = line.replace('Program: ', '')
                self.program = list(map(int, value.split(',')))

    def get_operand(self, combo):
        operand = self.program[self.ir]

        if (not combo):
            return operand

        if operand >= 0 and operand <= 3:
            return operand
        if operand == 4:
            return self.reg_a
        if operand == 5:
            return self.reg_b
        if operand == 6:
            return self.reg_c
        
    def run_program(self):
        while self.ir < len(self.program):
            op = self.program[self.ir]
            self.ir = self.ir + 1

            if op == 0: #adv
                numerator = self.reg_a
                denominator = self.get_operand(True)
                self.ir = self.ir + 1
                self.reg_a = numerator >> (denominator)
            elif op == 1: #bxl
                operand_1 = self.reg_b
                operand_2 = self.get_operand(False)
                self.ir = self.ir + 1
                self.reg_b = operand_1 ^ operand_2
            elif op == 2: #bst
                operand = self.get_operand(True)
                self.ir = self.ir + 1
                self.reg_b = operand & 0b0111
            elif op == 3: #jnz
                if self.reg_a == 0:
                    self.ir = self.ir + 1
                else:
                    self.ir = self.get_operand(False)
            elif op == 4: #bxc
                operand_1 = self.reg_b
                operand_2 = self.reg_c
                self.ir = self.ir + 1
                self.reg_b = operand_1 ^ operand_2
            elif op == 5: #out
                operand = self.get_operand(True)
                self.ir = self.ir + 1
                out = operand & 0b0111
                self.output.append(out)
            elif op == 6: #bdv
                numerator = self.reg_a
                denominator = self.get_operand(True)
                self.ir = self.ir + 1
                self.reg_b = numerator >> denominator
            elif op == 7: #cdv
                numerator = self.reg_a
                denominator = self.get_operand(True)
                self.ir = self.ir + 1
                self.reg_c = numerator >> denominator


    def solve(self):
        result = 0

        todo = [(len(self.program) - 1, 0)]
        while len(todo) > 0:
            off, val = todo.pop(0)
            for i in range(8):
                self.parse(self.input)
                next_val = (val << 3) + i
                self.reg_a = next_val
                self.run_program()
                if self.output == self.program[off:]:
                    todo.append((off - 1, next_val))
                    if (off == 0):
                        return next_val

        return None


            
                

    def print_state(self):
        print(f'Register A: ', self.reg_a)
        print(f'Register B: ', self.reg_b)
        print(f'Register C: ', self.reg_c)
        print()
        print(' ' * self.ir, end='v')
        print()
        print(''.join((str(x) for x in self.program)))
        print()
        print(','.join((str(x) for x in self.output)))
        



if __name__ == '__main__':
    file = open('input', 'r')
    a = Computer(file.read())
    print(a.solve())