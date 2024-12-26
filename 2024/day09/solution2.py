class Block:
    def __init__(self, id, start, size, is_free):
        self.id = id

        if is_free:
            self.id = '.'
        
        self.start = start
        self.size = size
        self.is_free = is_free
    
    def checksum(self):
        if self.is_free:
            return 0
        
        s = 0
        for i in range(self.size):
            s = s + (self.start + i) * int(self.id)
        return s


class Disk:

    def __init__(self, input):
        self.input = input
        self.parse(input)
    
    def parse(self, input):
        self.blocks = []

        nums = list(map(int, list(input)))
        curr_id = 0
        curr_index = 0
        for i in range(len(nums)):
            is_free = i % 2 == 1
            num = nums[i]

            self.blocks.append(Block(curr_id, curr_index, num, is_free))
            if not is_free:
                curr_id = curr_id + 1
            
            curr_index = curr_index + num


    def calculate_size(self, input):
        nums = list(map(int, list(input)))
        sum = 0
        for num in nums:
            sum = sum + num
        
        return sum

    def solve(self):
        files = list(filter(lambda x: not x.is_free, self.blocks))

        while len(files) > 0:
            print(len(files))
            self.blocks = sorted(self.blocks, key = lambda x: x.start)                 
            free_blocks = list(filter(lambda x: x.is_free, self.blocks))
            file = files.pop()

            for block in free_blocks:
                if file.size <= block.size and file.start > block.start:
                    block_remaining_size = block.size - file.size

                    if (block_remaining_size > 0):
                        new_block = Block('.', block.start + file.size, block_remaining_size, True)
                        self.blocks.append(new_block)

                    file.id, block.id = block.id, file.id
                    block.is_free = False
                    file.is_free = True
                    block.size = file.size
                    break




        self.blocks = filter(lambda x: x.size > 0, self.blocks)
        return self.calculate_checksum()

    def calculate_checksum(self):
        sum = 0
        for block in self.blocks:
            sum = sum + block.checksum()
        
        return sum

    def __str__(self):
        s = ''
        self.blocks = sorted(self.blocks, key = lambda x: x.start)
        for block in self.blocks:
            s = s + f'{block.id}' * block.size
        return s



if __name__ == '__main__':
    file = open('input', 'r')
    a = Disk(file.read())
    print(a)
    print(a.solve())
    print(a)
