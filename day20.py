class Particle:
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = Particle.getXYZ(p)
        self.v = Particle.getXYZ(v)
        self.a = Particle.getXYZ(a)
        self.start = (self.p, self.v, self.a)

    def getXYZ(e):
        nums = e[e.find('<')+1:e.find('>')].split(',')
        nums = [int(x) for x in nums]
        return nums

    def manhattan(self, x):
         return sum([abs(s) for s in x])

    def __str__(self):
        return 'id={}, p={}, v={}, a={}'.format(self.id,self.p,self.v,self.a)

    def move(self):
        for i in range(3):
            self.v[i] += self.a[i]
        for i in range(3):
            self.p[i] += self.v[i]

    def trend(self, r=100000):
        for i in range(r):
            self.move()
        return self.manhattan(self.p)

def loadParticles():
    particles = []
    id = 0
    input = open("inputs/day20.txt", "r")
    for line in input:
        p,v,a = line.strip().split(', ')
        part = Particle(id,p,v,a)
        particles.append(part)
        id += 1
    input.close()
    return particles



def part1():
    particles = loadParticles()
    particles.sort(key=lambda p: p.manhattan(p.a))
    for p in particles[:3]:
        print(p, p.manhattan(p.a), p.trend())

def part2():
    particles
