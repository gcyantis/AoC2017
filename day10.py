from functools import reduce

class Circle:
    def __init__(self, size):
        self.circleSize = size
        self.circle = [x for x in range(0,size)]

    def hash(self,lengths,rounds = 1):
        curPos = 0
        skipSize = 0
        for round in range(0,rounds):
            for length in lengths:
                pinch = self.circle[curPos:curPos+length]
                if curPos+length > self.circleSize : pinch += self.circle[:curPos+length-self.circleSize]
                pinch.reverse()
                for i in range(0,length):
                    self.circle[(curPos+i) % self.circleSize] = pinch[i]
                curPos = (curPos + length + skipSize) % self.circleSize
                skipSize += 1
        return self

    def quickCheck(self):
        return self.circle[0] * self.circle[1]

    def condenseHash(self):
        hash = ''
        blocks = [self.circle[16 * i : 16 * (i + 1)] for i in range(0,16)]
        for block in blocks:
            hash += "%0.2X" % reduce(lambda x, y: x^y, block)
        return hash

def p2lengths(string):
    return [ord(c) for c in string] + [17, 31, 73, 47, 23]

testLengths = [3, 4, 1, 5]
input = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'
part1Lengths = [106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36]

#print('Test: {}'.format(Circle(5).hash(testLengths).quickCheck()))
print('Part 1: {}'.format(Circle(256).hash(part1Lengths).quickCheck()))
#print('Test 2: {}'.format(Circle(256).hash(p2lengths(''),64).condenseHash()))
#print('Test 3: {}'.format(Circle(256).hash(p2lengths('AoC 2017'),64).condenseHash()))
print('Part 2: {}'.format(Circle(256).hash(p2lengths(input),64).condenseHash()))
