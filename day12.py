
class Pipes:
    connections = {}


    def addConnection(p1,p2):
        if p1 not in Pipes.connections: Pipes.connections[p1] = [p2]
        elif p2 not in Pipes.connections[p1]: Pipes.connections[p1].append(p2)

    def findGroup(program, group = []):
        group.append(program)
        for connection in Pipes.connections[program]:
            if connection not in group:
                group = Pipes.findGroup(connection, group)
        return group

    def findInGroups(program, groups):
        for group in groups:
            if program in group: return True
        return False

    def allGroups():
        groups = []
        for program in Pipes.connections:
            if not Pipes.findInGroups(program, groups):
                groups.append(Pipes.findGroup(program,[]))
        return groups


    def loadConnections(file):
        input = open("inputs/"+file+".txt", "r")
        for line in input:
            program, group = line.strip().split(' <-> ')
            program = int(program)
            group = [int(x) for x in group.split(', ')]
            for connection in group:
                Pipes.addConnection(program, connection)
                Pipes.addConnection(connection, program)
        input.close()


#Pipes.loadConnections("day12test")
Pipes.loadConnections("day12")
print('Part 1: {} programs in group[0]'.format(len(Pipes.findGroup(0))))
print('Part 2: {} groups'.format(len(Pipes.allGroups())))
