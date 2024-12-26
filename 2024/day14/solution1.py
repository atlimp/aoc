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
        for line in input.split('\n'):
            split = line.split(' ')
            pos = split[0][2::].split(',')
            vel = split[1][2::].split(',')

            self.robots.append(Robot(int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])))

        middle_x = width // 2
        middle_y = height // 2
        max_x = width - 1
        max_y = height - 1

        self.quadrants = []

        self.quadrants.append({
            'min': (0, 0),
            'max': (middle_x - 1, middle_y - 1),
            'count': 0
        })

        
        self.quadrants.append({
            'min': (middle_x + 1, 0),
            'max': (max_x, middle_y - 1),
            'count': 0
        })

        
        self.quadrants.append({
            'min': (0, middle_y + 1),
            'max': (middle_x - 1, max_y),
            'count': 0
        })

        
        self.quadrants.append({
            'min': (middle_x + 1, middle_y + 1),
            'max': (max_x, max_y),
            'count': 0
        })



    def solve(self, seconds):
        for robot in self.robots:
            end_x = (robot.x + (seconds * robot.vx)) % self.width
            end_y = (robot.y + (seconds * robot.vy)) % self.height

            for i in range(len(self.quadrants)):
                quadrant = self.quadrants[i]

                min_x, min_y = quadrant['min']
                max_x, max_y = quadrant['max']

                if end_x >= min_x and end_x <= max_x and end_y >= min_y and end_y <= max_y:
                    quadrant['count'] = quadrant['count'] + 1

        safety_factor = 1
        for quadrant in self.quadrants:
            safety_factor = safety_factor * quadrant['count']

        return safety_factor

    

if __name__ == '__main__':
    file = open('input', 'r')
    a = Floor(file.read(), 101, 103)
    print(a.solve(100))

