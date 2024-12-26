import itertools

KEYPAD_SYMBOLS = {
    'NONE': (3, 0),
    '0': (3,1),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    'A': (3,2),
}

DPAD_SYMBOLS = {
    'NONE': (0, 0),
    '^': (0,1),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
    'A': (0,2),
}

def sign(a):
    if a == 0:
        return 1
    if a < 0:
        return -1
    return 1



class Keypad:
    def __init__(self, symbols, symbol, parent, level):
        self.symbols = symbols
        self.symbol = symbol
        self.parent = parent
        self.level = level

    def move_to(self, from_symbol, to_symbol):
        orig_row, orig_col = self.symbols[from_symbol]
        
        new_row, new_col = self.symbols[to_symbol]

        d_row = new_row - orig_row
        d_col = new_col - orig_col

        moves = []
        if d_row != 0 and d_col == 0:
            token = 'v' if d_row > 0 else '^'
            moves.append(token * abs(d_row) + 'A')
            return moves
        if d_row == 0 and d_col != 0:
            token = '>' if d_col > 0 else '<'
            moves.append(token * abs(d_col) + 'A')
            return moves

        col_token = '>' if d_col > 0 else '<'
        row_token = 'v' if d_row > 0 else '^'

        initial_move = row_token * abs(d_row) + col_token * abs(d_col)

        for perm in list(itertools.permutations(initial_move)):
            if self.is_valid(perm, (orig_row, orig_col), self.symbols['NONE']):
                perm = ''.join(perm) + 'A'
                moves.append(perm)

        return moves
    
    def is_valid(self, moves, start, gap):
        row, col = start
        for move in list(moves):
            if move == '^':
                row = row - 1
            if move == '>':
                col = col + 1
            if move == 'v':
                row = row + 1
            if move == '<':
                col = col - 1

            if (row, col) == gap:
                return False
        
        return True
    
    def manhattan_distance(self, from_symbol, to_symbol):
        orig_row, orig_col = self.symbols[from_symbol]
        
        self.symbol = to_symbol
        new_row, new_col = self.symbols[self.symbol]

        d_row = new_row - orig_row
        d_col = new_col - orig_col

        return abs(d_row) + abs(d_col)

class Day21:
    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.codes = input.split('\n')
        self.d_pad2 = Keypad(DPAD_SYMBOLS, 'A', None, '2')
        self.d_pad1 = Keypad(DPAD_SYMBOLS, 'A', self.d_pad2, '1')
        self.keypad = Keypad(KEYPAD_SYMBOLS, 'A', self.d_pad1, '0')

    def move(self, from_symbol, to_symbol, keypad):

        if keypad.parent is None:
            return keypad.manhattan_distance(from_symbol, to_symbol) + 1
        
        moves_list = keypad.move_to(from_symbol, to_symbol)

        min_result = float('inf')
        for moves in moves_list:
            result = 0
            prev_symbol = 'A'
            for move in list(moves):
                result = result + self.move(prev_symbol, move, keypad.parent)
                prev_symbol = move
            if result < min_result:
                min_result = result
        
        return min_result

    def solve(self):

        result = 0

        for code in self.codes:
            complexity = 0
            prev_symbol = 'A'
            for symbol in list(code):
                complexity = complexity + self.move(prev_symbol, symbol, self.keypad)
                prev_symbol = symbol
            
            numeric_val = int(code.replace('A', ''))
            print(f'{code}: {complexity} * {numeric_val}')
            result = result + numeric_val * complexity

        return result

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day21(file.read())
    print(a.solve())



