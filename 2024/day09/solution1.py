class Disk:

    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.size = self.calculate_size(input)
        self.blocks = list(range(self.size))

        nums = list(map(int, list(input)))
        curr_index = 0
        curr_id = 0
        for i in range(len(nums)):
            is_free = i % 2 == 1
            num = nums[i]
            for j in range(num):
                token = '.'
                if not is_free:
                    token = curr_id

                self.blocks[curr_index] = token
                curr_index = curr_index + 1

            if not is_free:
                curr_id = curr_id + 1


    def calculate_size(self, input):
        nums = list(map(int, list(input)))
        sum = 0
        for num in nums:
            sum = sum + num
        
        return sum
    
    def get_leftmost(self):
        return self.blocks.index('.')
    
    def get_rightmost(self):
        lis = list(filter(lambda x: x[1] != '.', enumerate(self.blocks)))
        return sorted(lis, key = lambda x: x[0], reverse=True)[0][0]

    def solve(self):
        leftmost_free = self.get_leftmost()
        rightmost_block = self.get_rightmost()

        print(f'Left: {leftmost_free}, Right: {rightmost_block}')

        while leftmost_free < rightmost_block:
            self.blocks[leftmost_free], self.blocks[rightmost_block] = self.blocks[rightmost_block], self.blocks[leftmost_free]

            while self.blocks[leftmost_free] != '.':
                leftmost_free = leftmost_free + 1

            while self.blocks[rightmost_block] == '.':
                rightmost_block = rightmost_block - 1

        print('Done swapping, calculating checksum')

        return self.calculate_checksum()

    def calculate_checksum(self):
        sum = 0
        for i in range(len(self.blocks)):
            tok = self.blocks[i]
            if tok != '.':
                sum = sum + tok * i
        
        return sum

    def __str__(self):
        s = ''
        for tok in self.blocks:
            s = s + f'{tok}'
        s = s + '\n'
        return s



if __name__ == '__main__':
    file = open('input', 'r')
    a = Disk(file.read())
    print(a)
    print(a.solve())