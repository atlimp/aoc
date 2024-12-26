BIG_NUMBER = 16777216

class RandomGen:
    def __init__(self, secret):
        self.secret = secret
        self.ones = []
        self.changes = []

        ones_digit = int(f'{self.secret}'[-1])
        self.ones.append(ones_digit)

        self.changes.append(None)

        self.seq = {}
    
    def get_next(self):

        #Step 1
        #Multiply with 64
        result = self.secret << 6

        result = result ^ self.secret
        result = result % BIG_NUMBER

        self.secret = result

        #Step 2
        result = result >> 5

        result = result ^ self.secret
        result = result % BIG_NUMBER

        self.secret = result

        #Step 3
        result = result << 11

        result = result ^ self.secret
        result = result % BIG_NUMBER

        self.secret = result

        ones_digit = int(f'{self.secret}'[-1])
        last_digit = self.ones[-1]
        self.ones.append(ones_digit)

        self.changes.append(ones_digit - last_digit)

        return self.secret
    
    def create_sequences(self):

        for i in range(1, len(self.changes) - 3):
            seq = self.changes[i:i + 4]

            seq_key = ','.join(map(str, seq))
            if seq_key not in self.seq:
                self.seq[seq_key] = self.ones[i + 3]
    
class Day22:
    def __init__(self, input):
        self.input = input
        self.nums = []
        self.parse(input)
    
    def parse(self, input):
        for line in input.split('\n'):
            secret = int(line)
            rand = RandomGen(secret)

            result = secret
            for i in range(2000):
                #print(f'{rand.secret}: {rand.ones[-1]} ({rand.changes[-1]})')
                result = rand.get_next()

            rand.create_sequences()
            
            self.nums.append(rand)

    def solve(self):

        dict = {}
        for num in self.nums:
            for seq_key in num.seq.keys():
                if seq_key not in dict:
                    dict[seq_key] = 0
                
                dict[seq_key] = dict[seq_key] + num.seq[seq_key]
        
        sorted_items = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

        return sorted_items[0]
            

if __name__ == '__main__':
    file = open('input', 'r')
    a = Day22(file.read())
    print(a.solve())


    