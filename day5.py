def part_1():
    numSteps = 0
    instructions = []
    #load instructions
    input = open("inputs/day5.txt", "r")
    for line in input:
        instructions.append(int(line.strip()))
    input.close()

    i = 0
    while True:
        j = instructions[i]
        instructions[i] += 1
        i += j
        numSteps += 1
        if i < 0 or i >= len(instructions):
            break

    print(numSteps)
part_1()

def part_2():
    numSteps = 0
    instructions = []
    #load instructions
    input = open("inputs/day5.txt", "r")
    for line in input:
        instructions.append(int(line.strip()))
    input.close()

    i = 0
    while True:
        j = instructions[i]
        if j >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1

        i += j
        numSteps += 1
        if i < 0 or i >= len(instructions):
            break

    print(numSteps)
part_2()
