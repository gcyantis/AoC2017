functions = {
    'inc' : lambda x,y : x + y,
    'dec' : lambda x,y : x - y,
    '>' : lambda x,y : x > y,
    '<' : lambda x,y : x < y,
    '>=' : lambda x,y : x >= y,
    '<=' : lambda x,y : x <= y,
    '==' : lambda x,y : x == y,
    '!=' : lambda x,y : x != y,
}

registers = {}
maxEver = 0

input = open("inputs/day8.txt", "r")
for line in input:
    r, pm, v, i, x, cond, y = line.strip().split()
    if r not in registers: registers[r] = 0
    if x not in registers: registers[x] = 0
    if functions[cond](registers[x],int(y)):
        registers[r] = functions[pm](registers[r],int(v))
        if registers[r] > maxEver: maxEver = registers[r]
input.close()

print(registers)
print(registers[max(registers, key=registers.get)])
print(maxEver)
