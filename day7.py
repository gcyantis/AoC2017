class Program:
    programs = {}

    def __init__(self, name, weight, tower):
        self.name = name
        self.weight = weight
        self.tower = tower

    def __str__(self):
        return str(self.name) + ' (' + str(self.weight) + ')'

    def print_program_indented(program, level=0):
        if program == None: return
        print('  ' * level + str(program))
        #for p in program.tower:
            #Program.print_program_indented(p, level+1)

input = open("inputs/day7test.txt", "r")
for line in input:
    sp = line.split(' -> ')
    name, weight = sp[0].split()
    weight = int(weight.strip('()'))
    if len(sp) > 1:
        tower = sp[1].split(', ')
    else:
        tower = ''
    Program.programs[name] = Program(name,weight,tower)

print(Program.print_program_indented(Program.programs['tknk']))
