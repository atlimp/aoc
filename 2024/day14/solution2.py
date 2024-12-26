class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

class Floor:
    def __init__(self, input, width, height):
        self.robots = []
        self.width = width
        self.height = height

        self.clear_grid()

        for line in input.split('\n'):
            split = line.split(' ')
            pos = split[0][2::].split(',')
            vel = split[1][2::].split(',')

            self.robots.append(Robot(int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])))

    def clear_grid(self):
        self.grid = []

        for row in range(self.height):
            self.grid.append([])
            for col in range(self.width):
                self.grid[row].append('.')

    def solve(self):
        run = input('')
        seconds = 87

        while run != 'n':
            self.clear_grid()
            for robot in self.robots:
                end_x = (robot.x + (seconds * robot.vx)) % self.width
                end_y = (robot.y + (seconds * robot.vy)) % self.height


                self.grid[end_y][end_x] = 'X'
            
            print(self)
            print(seconds)
            seconds = seconds + 103
            run = input('')


    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s = s + col
            s = s + '\n'
        
        return s
                
        

    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Floor(file.read(), 101, 103)
    print(a.solve())

