from functools import reduce
from colorconsole import terminal
from copy import deepcopy

class KnotHash:
    def __init__(self, key, size = 256):
        self.key = key
        self.circleSize = size
        self.circle = [x for x in range(0,size)]

        self.lengths = self.makeLengths(self.key)
        self.makeHash()
        self.hash = self.condenseHash()

    def makeLengths(self,string):
        return [ord(c) for c in string] + [17, 31, 73, 47, 23]

    def makeHash(self,rounds = 64):
        curPos = 0
        skipSize = 0
        for round in range(0,rounds):
            for length in self.lengths:
                pinch = self.circle[curPos:curPos+length]
                if curPos+length > self.circleSize : pinch += self.circle[:curPos+length-self.circleSize]
                pinch.reverse()
                for i in range(0,length):
                    self.circle[(curPos+i) % self.circleSize] = pinch[i]
                curPos = (curPos + length + skipSize) % self.circleSize
                skipSize += 1
        return self

    def condenseHash(self):
        hash = ''
        blocks = [self.circle[16 * i : 16 * (i + 1)] for i in range(0,16)]
        for block in blocks:
            hash += "%0.2X" % reduce(lambda x, y: x^y, block)
        return hash.lower()

    def binaryHash(self):
        return bin(int(self.hash, 16))[2:].zfill(128)

class Disk:
    def __init__(self, key):
        self.key = key
        self.rows = []
        self.buildDisk()

    def buildDisk(self):
        for row in range(0,128):
            self.rows.append(KnotHash(input+'-'+str(row)).binaryHash())

    def calcUsed(self):
        used = 0
        for row in self.rows:
            used += row.count('1')
        return used

    def findRegions(self):
        self.regions = [[None for x in range(0,128)] for y in range(0,128)]
        self.numRegions = 1
        for y in range(0,128):
            for x in range(0,128):
                if self.rows[y][x] == '1' and self.regions[y][x] == None:
                    self.fillAdjacent(x,y,self.numRegions)
                    self.numRegions += 1

        self.numRegions -= 1 #account for extra added at end
        return self.numRegions

    def fillAdjacent(self, x, y, regionNum):
        self.regions[y][x] = regionNum
        for ax, ay in [(0,1),(1,0),(0,-1),(-1,0)]:
            dx, dy = x+ax, y+ay
            if dx >= 0 and dy >= 0 and dx <= 127 and dy <= 127 and self.rows[dy][dx] == '1' and self.regions[dy][dx] == None:
                self.fillAdjacent(dx,dy,regionNum)

    def __str__(self):
        string = ''
        for row in self.rows:
            string += row.replace('1','#').replace('0','-') + '\n'
        return string

    def printRegions(self):
        screen = terminal.get_terminal(conEmu=False)
        screen.clear()
        screen.print_at(0,0,"Fragmented Disk")
        for y in range(0,128):
            for x in range(0,128):
                if self.regions[y][x]:
                    screen.gotoXY(x,y+1)
                    screen.cprint(0,self.regions[y][x]%15+1, " ")
        screen.reset_colors()
        screen.getch()

def runTests():
    testHashes = [
        ('','a2582a3a0e66e6e86e3812dcb672a272'),
        ('AoC 2017','33efeb34ea91902bb2f59c9920caa6cd'),
        ('1,2,3','3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4','63960835bcdc130f0b66d7ff4f6a5a8e'),
    ]
    print('Tests\n'+'-'*40)
    for key, hash in testHashes:
        knot = KnotHash(key)
        print(knot.hash, knot.hash == hash)
        #print(knot.binaryHash())



#runTests()
#input = 'flqrgnkx'
input = 'amgozmfv'
disk = Disk(input)
disk.findRegions()
disk.printRegions()
print('\n\nPart 1: {} bits used'.format(disk.calcUsed()))
print('Part 2: {} regions'.format(disk.numRegions))
