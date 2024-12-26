class Stone:
    def __init__(self, data):
        self.data = data
        self.next = None

    def blink(self):
        if self.data == 0:
            self.data = 1
            return self.next
        if len(f'{self.data}') % 2 == 0:
            string_data = f'{self.data}'
            len_data = len(string_data)
            a = int(string_data[0:(len_data//2)])
            b = int(string_data[len_data//2:len_data])

            self.data = a
            new_stone = Stone(b)
            a_next = self.next
            self.next = new_stone
            new_stone.next = a_next
            return new_stone.next
        else:
            self.data = self.data * 2024
            return self.next
           



class Line:
    def __init__(self, input):
        self.input = input
        self.head = None
        self.parse(input)

    def parse(self, input):
        lis = list(map(int, input.split(' ')))
        for el in lis:
            self.append(Stone(el))

    def append(self, stone):
        if (self.head is None):
            self.head = stone
            return
        
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        
        curr_node.next = stone

    def solve(self):
        for i in range(25):
            print(f'After {i + 1} blinks')
            next_node = self.head.blink()
            while next_node is not None:
                next_node = next_node.blink()

        return self.size()


    def size(self):
        size = 0
        curr_node = self.head
        while curr_node is not None:
            size = size + 1
            curr_node = curr_node.next
        return size
    
    def __str__(self):
        s = ''
        curr_node = self.head
        while curr_node is not None:
            s = s + f'{curr_node.data} '
            curr_node = curr_node.next
        return s
    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Line(file.read())
    print(a)
    print(a.solve())