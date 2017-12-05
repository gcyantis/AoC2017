import math

def part_1():
    input = 277678

    square = math.sqrt(input)
    nextSquare = math.ceil(square)

    if nextSquare % 2 == 0:
        width = nextSquare + 1
    else:
        width = nextSquare

    # Might not work for everything, c1 should be dependent on evenness, and be w-2 if even
    c1 = math.pow(width,2)
    c2 = math.ceil(math.pow(nextSquare-0.5,2))
    c3 = math.pow(width-1,2)+1
    distFromCorner = min(map(abs, (input-c1, input-c2, input-c3)))
    distance = width - 1 - distFromCorner

    print(distance)

class Spiral:
    def __init__(self):
        self.coords = {0:{0:1}}
        self.curX = 0
        self.curY = 0
        self.curV = 1
        self.width = 0
        self.directions = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
        self.heading = 0

    def addNext(self, method):
        if self.curX + self.curY == 0 and self.curX == self.width:
            self.width += 1
            nextX = self.width
            nextY = self.curY
            self.heading = 0
            self.coords[self.width] = {}
            self.coords[-self.width] = {}
        else:
            if abs(self.curX) == self.width and abs(self.curY) == self.width:
                self.heading = (self.heading + 1) % 4

            dx, dy = self.directions[self.heading]
            nextX = self.curX + dx
            nextY = self.curY + dy

        self.curX, self.curY = nextX, nextY

        if method == 'inc':
            self.curV += 1
        elif method == 'surrounding':
            self.curV = self.sumSurrounding(self.curX,self.curY)

        self.coords[self.curX][self.curY] = self.curV

    def sumSurrounding(self, x, y):
        sum = 0
        surrounding = [(0,1),(-1,0),(0,-1),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        for d in surrounding:
            dx, dy = d
            a = x + dx
            b = y + dy
            if a in self.coords:
                if b in self.coords[a]:
                    sum += self.coords[a][b]
        return sum

    def display(self):
        for y in range(self.width, -self.width-1, -1):
            for x in range(-self.width, self.width+1):
                print('{0:3d}'.format(self.coords[x][y]),end='  ')
            print()

def part_2():
    sp = Spiral()
    while sp.curV < 277678:
        sp.addNext('surrounding')
    print(sp.curV)

print('Part 1:')
part_1()

print('\nPart 2:')
part_2()
