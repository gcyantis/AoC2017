class Program:
    programs = {}
    fixWeight = 0

    def __init__(self, name, weight, tower):
        self.name = name
        self.weight = weight
        self.tower = tower
        self.balanced = 0
        self.balance = 0

    def __str__(self):
        return '{} ({}) : ({},{})'.format(self.name,self.weight,self.balanced,self.balance)

    def print_program_indented(self, level=0):
        print('  ' * level + str(self))
        for p in self.tower:
            Program.print_program_indented(self.tower[p], level+1)

    def find_program(name, programs):
        if name in programs: return programs.pop(name)
        for p in programs:
            program = Program.find_program(name,programs[p].tower)
            if program != None: return program
        return None

    def build_tower(programs):
        keys = list(programs.keys())
        for key in keys:
            if key in programs:
                programs[key] = Program.fill_tower(programs, programs[key])
        return programs

    def fill_tower(programs, program):
        for name in program.tower:
            program.tower[name] = Program.find_program(name, programs)
            program.tower[name] = Program.fill_tower(programs, program.tower[name])
        program.check_balance()
        return program

    def check_balance(self):
        if len(self.tower) == 0:
            self.balanced = True
            self.balance = self.weight
        else:
            weights = [self.tower[t].balance for t in self.tower]
            self.balanced = weights.count(weights[0]) == len(weights)
            self.balance = sum(weights) + self.weight
        if not self.balanced and Program.fixWeight == 0:
            oddWeight = [i for i in weights if weights.count(i) == 1][0]
            modeWeight = [i for i in set(weights) if i != oddWeight][0]
            toFix = [self.tower[t] for t in self.tower if self.tower[t].balance == oddWeight][0]
            Program.fixWeight = toFix.weight + modeWeight - oddWeight
            Program.toFix = toFix

input = open("inputs/day7.txt", "r")
programs = {}
for line in input:
    sp = line.split(' -> ')
    name, weight = sp[0].split()
    weight = int(weight.strip('()'))
    if len(sp) > 1:
        tower = sp[1].strip().split(', ')
        tower = dict([(n,Program(n,0,{})) for n in tower])
    else:
        tower = {}
    programs[name] = Program(name,weight,tower)
input.close()

programs = Program.build_tower(programs)
print(programs.keys())
#for p in programs:
    #programs[p].print_program_indented()
print(Program.fixWeight)
print('To fix: '+str(Program.toFix))
