registers = {}
instructons = []

input = open("inputs/day18.txt", "r")
for line in input:
    instruction = line.strip().split()
    if len(instruction) < 3: instruction.append(None)
    if instruction[1].isalpha() and instruction[1] not in registers: registers[instruction[1]] = 0
    elif not instruction[1].isalpha(): instruction[1] = int(instruction[1])
    if instruction[2] != None and not instruction[2].isalpha(): instruction[2] = int(instruction[2])
    instructons.append(instruction)
input.close()

def part1():
    played = 0
    i = 0
    while 0 <= i and i < len(instructons):
        #print(i, instructons[i])
        funct, x, y = instructons[i]
        if y in registers:
            y = registers[y]

        if funct == 'snd':
            played = registers[x]
        elif funct == 'set':
            registers[x] = y
        elif funct == 'add':
            registers[x] += y
        elif funct == 'mul':
            registers[x] *= y
        elif funct == 'mod':
            registers[x] %= y
        elif funct == 'rcv':
            if registers[x] != 0:
                break
        elif funct == 'jgz':
            if registers[x] > 0:
                i += y
            else:
                i+=1
        if funct != 'jgz':
            i += 1
    print(played)



def runInstruction(program, partner):
    funct, x, y = instructons[program['line']]
    if y in program:
        y = program[y]

    if funct == 'snd':
        partner['queue'].append(program[x])
        program['sent'] += 1
    elif funct == 'rcv':
        if len(program['queue']):
            program[x] = program['queue'].pop(0)
            program['state'] = ''
        else:
            program['line'] -= 1 #cancel out auto advance to hold
            program['state'] = 'waiting'
    elif funct == 'set':
        program[x] = y
    elif funct == 'add':
        program[x] += y
    elif funct == 'mul':
        program[x] *= y
    elif funct == 'mod':
        program[x] %= y
    elif funct == 'jgz':
        if (x in program and program[x] > 0) or (x not in program and x > 0):
            program['line'] += y
        else:
            program['line'] += 1
    if funct != 'jgz':
        program['line'] += 1

def ready(program):
    notWaiting = program['state'] != 'waiting' or len(program['queue'])
    inRange = program['line'] >= 0 and program['line'] < len(instructons)
    return notWaiting and inRange

def part2():
    registers['state'] = ''
    registers['sent'] = 0
    registers['line'] = 0

    A = registers.copy()
    A['p'] = 0
    A['queue'] = []
    B = registers.copy()
    B['p'] = 1
    B['queue'] = []

    while ready(A) or ready(B):
        while ready(A):
            runInstruction(A, B)
        while ready(B):
            runInstruction(B, A)

        #print('0', A['line'], '1', B['line'], B['sent'])

    print('0', A)
    print('1', B)

#part1()
part2()
