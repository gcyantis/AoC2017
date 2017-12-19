class Program:
    def __init__(self, registers, id, instructions, partner = None):
        self.registers = registers
        self.registers['p'] = id
        self.id = id
        self.partner = partner
        self.state = ''
        self.sent = 0
        self.line = 0
        self.queue = []
        self.instructions = instructions

    def ready(self):
        notWaiting = self.state != 'waiting' or len(self.queue)
        inRange = self.line  >= 0 and self.line < len(self.instructions)
        return notWaiting and inRange

    def next(self):
        funct, x, y = self.instructions[self.line]
        if y in self.registers:
            y = self.registers[y]

        if funct == 'snd':
            if x in self.registers:
                self.partner.queue.append(self.registers[x])
            else:
                self.partner.queue.append(x)
            self.sent += 1
        elif funct == 'rcv':
            if len(self.queue):
                self.registers[x] = self.queue.pop(0)
                self.state = ''
            else:
                self.line -= 1 #cancel out auto advance to hold
                self.state = 'waiting'
        elif funct == 'set':
            self.registers[x] = y
        elif funct == 'add':
            self.registers[x] += y
        elif funct == 'mul':
            self.registers[x] *= y
        elif funct == 'mod':
            self.registers[x] %= y
        elif funct == 'jgz':
            if (x in self.registers and self.registers[x] > 0) or (x not in self.registers and x > 0):
                self.line += y
            else:
                self.line += 1
        if funct != 'jgz':
            self.line += 1

class Duet:
    def __init__(self, file = ''):
        self.loadInstructions(file)
        self.p0 = Program(self.registers.copy(), 0, self.instructions)
        self.p1 = Program(self.registers.copy(), 1, self.instructions, self.p0)
        self.p0.partner = self.p1

        self.play()


    def loadInstructions(self, file):
        self.registers = {}
        self.instructions = []
        input = open("inputs/day18"+file+".txt", "r")
        for line in input:
            instruction = line.strip().split()
            if len(instruction) < 3: instruction.append(None)
            if instruction[1].isalpha() and instruction[1] not in self.registers: self.registers[instruction[1]] = 0
            elif not instruction[1].isalpha(): instruction[1] = int(instruction[1])
            if instruction[2] != None and not instruction[2].isalpha(): instruction[2] = int(instruction[2])
            self.instructions.append(instruction)
        input.close()

    def play(self):
        while self.p0.ready() or self.p1.ready():
            while self.p0.ready():
                self.p0.next()
            while self.p1.ready():
                self.p1.next()

D = Duet()
print(D.p1.registers, D.p1.sent)
