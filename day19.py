class MapRunner:
    directions = {
        'N':(0,-1),
        'S':(0,1),
        'E':(1,0),
        'W':(-1,0)
    }

    def __init__(self, file=''):
        self.diagram = MapRunner.getMap(file)
        self.letters = []
        self.x = self.diagram[0].index('|')
        self.y = 0
        self.heading = 'S'
        self.steps = 1

        self.followDirections()

    def move(self):
        a, b = MapRunner.directions[self.heading]
        self.x += a
        self.y += b
        self.steps += 1
        #print(self.x, self.y, self.curChar())
        if self.curChar().isalpha():
            self.letters.append(self.curChar())

    def getMap(file=''):
        diagram = []
        input = open("inputs/day19"+file+".txt", "r")
        for line in input:
            #print(line[:-1])
            diagram.append([c for c in line[:-1]])
        input.close()
        return diagram

    def checkHeading(self, heading):
        a, b = MapRunner.directions[heading]
        nx = self.x + a
        ny = self.y + b
        if ny < 0 or len(self.diagram) <= ny or nx < 0 or len(self.diagram[ny]) <= nx:
            return False #out of bounds
        return not self.diagram[ny][nx].isspace()

    def curChar(self):
         return self.diagram[self.y][self.x]

    def followDirections(self):
        while True:
            if self.checkHeading(self.heading):
                self.move()
            else:
                if self.heading in 'NS':
                    if self.checkHeading('E'):
                        self.heading = 'E'
                        self.move()
                    elif self.checkHeading('W'):
                        self.heading = 'W'
                        self.move()
                    else:
                        break
                else:
                    if self.checkHeading('N'):
                        self.heading = 'N'
                        self.move()
                    elif self.checkHeading('S'):
                        self.heading = 'S'
                        self.move()
                    else:
                        break

M = MapRunner()
print('Part 1: Path followed = '+''.join(M.letters))
print('Part 2: {} steps'.format(M.steps))
