class Generator:
    def __init__(self, factor, start, multiple = 1):
        self.preVal = start
        self.factor = factor
        self.multiple = multiple
    def next(self):
        nextVal = (self.preVal * self.factor) % 2147483647
        self.preVal = nextVal
        if nextVal % self.multiple != 0:
            self.next()
        return self.preVal

class Judge:
    def __init__(self):
        self.count = 0
    def judge(self, a, b):
        if a & 0xFFFF == b & 0xFFFF: self.count += 1

def test():
    genA = Generator(16807, 65, 4)
    genB = Generator(48271, 8921, 8)
    judge = Judge()
    print('--Gen. A--  --Gen. B--')
    for i in range(5):
        a, b = genA.next(), genB.next()
        print('{:10}  {:10}'.format(a,b))
        judge.judge(a, b)
    print(judge.count)

#test()

#genA = Generator(16807, 65)
#genB = Generator(48271, 8921)

def part1():
    genA = Generator(16807, 591)
    genB = Generator(48271, 393)

    judge = Judge()
    for i in range(40000000):
        judge.judge(genA.next(), genB.next())
    print('Part 1: Final count {}'.format(judge.count))

def part2():
    genA = Generator(16807, 591, 4)
    genB = Generator(48271, 393, 8)
    judge = Judge()
    for i in range(5000000):
        judge.judge(genA.next(), genB.next())
    print('Part 2: Final count {}'.format(judge.count))

#part1()
part2()
