from collections import Counter

def noDuplicates(phrase):
    words = phrase.split()
    counts = list(Counter(words))
    return len(words) == len(counts)

def noAnagrams(phrase):
    words = phrase.split()
    counts = [Counter(w) for w in words]
    unique = [c for n, c in enumerate(counts) if c not in counts[n+1:]]
    return len(words) == len(unique)

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
