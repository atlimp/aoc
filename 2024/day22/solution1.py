BIG_NUMBER = 16777216

class RandomGen:
    def __init__(self, secret):
        self.secret = secret
    
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

        return self.secret

if __name__ == '__main__':
    file = open('input', 'r')
    input = file.read()

    sum = 0
    for line in input.split('\n'):
        secret = int(line)
        rand = RandomGen(secret)

        result = secret
        for i in range(2000):
            result = rand.get_next()
        
        sum = sum + result
        print(f'{secret}: {result}')
    
    print(sum)
    