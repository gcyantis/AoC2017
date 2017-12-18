layers = {}

def studyFirewall(file):
    input = open("inputs/"+file+".txt", "r")
    for line in input:
        d, r = line.strip().split(': ')
        layers[int(d)] = int(r)
    input.close()

def checkCaught(pos, time):
    if pos not in layers: return False
    depth = layers[pos]
    scannerPos = time % (depth * 2 - 2)
    #check if moving back towards 0
    if scannerPos >= depth: scannerPos = (depth - 1) * 2 - scannerPos
    return scannerPos == 0

def hitchRide():
    caught = []
    for curPos in range(0,max(layers)+1):
        if checkCaught(curPos,curPos):
            caught.append(curPos)
    return sum([layer * layers[layer] for layer in caught])

def cleanRide(delay):
    for curPos in range(0,max(layers)+1):
        if checkCaught(curPos,curPos+delay): return False
    return True

studyFirewall('day13')

print('Part 1: Severity of ride is '+str(hitchRide()))

delay = 0
while not cleanRide(delay):
    delay += 1
print('Part 2: Delay {} picoseconds to remain undetected'.format(delay))
