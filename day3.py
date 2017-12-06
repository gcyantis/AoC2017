import math

def spiralTest(method):
    sp = Spiral()
    while sp.width < 3:
        sp.addNext(method)
    sp.width -= 1
    sp.display()

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
    directions = [(0,1),(-1,0),(0,-1),(1,0)]
    
    def __init__(self):
        self.coords = {0:{0:1}}
        self.x = 0
        self.y = 0
        self.val = 1
        self.width = 0
        self.heading = 0

    def addNext(self, method):
        if self.x + self.y == 0 and self.x == self.width:
            self.width += 1
            self.x = self.width
            self.heading = 0
            self.coords[self.width] = {}
            self.coords[-self.width] = {}
        else:
            if abs(self.x) == self.width and abs(self.y) == self.width:
                self.heading = (self.heading + 1) % 4
            dx, dy = Spiral.directions[self.heading]
            self.x += dx
            self.y += dy

        if method == 'inc':
            self.val += 1
        elif method == 'surrounding':
            self.val = self.sumSurrounding(self.x,self.y)

        self.coords[self.x][self.y] = self.val

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
    while sp.val < 277678:
        sp.addNext('surrounding')
    print(sp.val)

print('Part 1: ', end='')
part_1()
spiralTest('inc')

print('\nPart 2: ', end='')
part_2()
spiralTest('surrounding')
