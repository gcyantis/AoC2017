def part_1():
    #banks = [0,2,7,0]
    input = open("inputs/day6.txt", "r")
    banks = input.readline().strip().split('\t')
    input.close()
    banks = [int(b) for b in banks]

    print(banks)

    states = []
    cycles = 0
    while banks not in states:
        states.append(banks.copy())
        redist = banks.index(max(banks))
        blocks = banks[redist]
        banks[redist]=0
        for i in range(1,blocks+1):
            banks[(redist+i)%len(banks)] += 1
        cycles += 1
        #print(banks)

    print('Part 1: {0} cycles'.format(cycles))
    print('Part 2: {0} cycles'.format(cycles - states.index(banks)))

part_1()
