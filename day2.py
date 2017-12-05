def part_1():
    checksum = 0

    input = open("inputs/day2.txt", "r")
    for line in input:
        cells = line.strip().split('\t')
        cells = list(map(int, cells))
        checksum += max(cells) - min(cells)
    input.close()

    print(checksum)
part_1()

def part_2():
    checksum = 0

    input = open("inputs/day2.txt", "r")
    for line in input:
        cells = line.strip().split('\t')
        cells = list(map(int, cells))
        found = False
        for i in (range(0,len(cells))):
            if not found:
                for n in (range(i+1,len(cells))):
                    x,y = cells[i], cells[n]
                    if x%y == 0 or y%x == 0:
                        if x%y == 0:
                            checksum += x//y
                        elif y%x == 0:
                            checksum += y//x
                        found = True
                        break
    input.close()

    print(checksum)
part_2()
