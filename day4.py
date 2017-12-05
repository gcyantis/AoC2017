from collections import Counter

def noDuplicates(phrase):
    v = True
    words = phrase.split()
    counts = list(Counter(words))
    if len(words) > len(counts):
        v = False
    return v

def noAnagrams(phrase):
    v = True
    words = phrase.split()
    counts = [Counter(w) for w in words]
    for c in range(0,len(counts)-1):
        if v:
            for b in range(c+1,len(counts)):
                if counts[c] == counts[b]:
                    v = False
                    break
    return v

def part_1():
    validPasses = 0

    input = open("inputs/day4.txt", "r")
    for line in input:
        if noDuplicates(line.strip()):
            validPasses += 1
    input.close()

    print(validPasses)

def part_2():
    validPasses = 0

    input = open("inputs/day4.txt", "r")
    for line in input:
        if noAnagrams(line.strip()):
            validPasses += 1
    input.close()

    print(validPasses)

part_1()
part_2()
