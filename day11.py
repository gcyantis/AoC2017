class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.furthest = 0

    def move(self, dir):
        cubeDirections = {
            'n' : Cube(0, 1, -1),
            'ne' : Cube(1, 0, -1),
            'se' : Cube(1, -1, 0),
            's' : Cube(0, -1, 1),
            'sw' : Cube(-1, 0, 1),
            'nw' : Cube(-1, 1, 0)
        }
        m = cubeDirections[dir]
        self.x += m.x
        self.y += m.y
        self.z += m.z
        return self

    def followPath(self, path):
        for step in path:
            self.move(step)
            if self.cubeDistance(Cube(0,0,0)) > self.furthest: self.furthest = self.cubeDistance(Cube(0,0,0))
        return self

    def cubeDistance(self,b):
        return max(abs(self.x - b.x), abs(self.y - b.y), abs(self.z - b.z))

def tests():
    tests = [("ne,ne,ne", 3),("ne,ne,sw,sw",0),("ne,ne,s,s",2),("se,sw,se,sw,sw",3)]
    for test in tests:
        path, expected = test
        test = Cube(0,0,0)
        test.followPath(path.split(','))
        dist = test.cubeDistance(Cube(0,0,0))
        print('{}, Steps: {}, Pass: {}'.format(path,dist, dist==expected))

#tests()

f = open("inputs/day11.txt", "r")
input = f.readline().strip().split(',')
f.close()

dayCube = Cube(0,0,0).followPath(input)

print('Part 1: {} steps away'.format(dayCube.cubeDistance(Cube(0,0,0))))
print('Part 2: {} steps away'.format(dayCube.furthest))
