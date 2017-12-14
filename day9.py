import re

def find_groups(string, depth = 1):
    items = []
    if len(string) < 2: return items
    #print(string)

    openBr, start = 0,0

    for c in range(0,len(string)):
        if openBr == 0 and string[c] == '{':
            start = c

        if string[c] == '{': openBr += 1
        elif string[c] == '}': openBr -= 1

        if openBr == 0 and string[c] == '}':
            item = string[start:c+1]
            items.append((item,depth))
            items.extend(find_groups(string[start+1:c],depth+1))

    return items

def score_groups(string):
    return sum([x[1] for x in find_groups(string)])

def count_trash(trash):
    return sum([len(x) - (x.count('!')*2) - 2 for x in trash])

input = open("inputs/day9.txt", "r")
string = input.readline().strip()
input.close()
#string = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
removeDoubleNeg = re.compile("!!")
removeTrash = re.compile("(<.*?(?<!!)>)")

string = removeDoubleNeg.sub('', string)

trash = removeTrash.findall(string)
string = removeTrash.sub('', string)

#print('Start ' + test_str)
#print(find_groups(string))
print('Part 1: {}'.format(score_groups(string)))
print('Part 2: {}'.format(count_trash(trash)))
