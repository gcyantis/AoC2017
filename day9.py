import re

def score_groups(string, depth = 1):
    print(string)

    openBr, start = 0,0
    items = []
    for c in range(0,len(string)):
        if openBr == 0: start = c

        if string[c] == '{': openBr += 1
        elif string[c] == '}': openBr -= 1

        if openBr == 0:
            item = string[start:c]
            items.append(item)
            items.extend(score_groups(item[1:-1],depth+1))

    return items


test_str = "{{{},{},{{}}}}"
removeDoubleNeg = re.compile("!!")
removeTrash = re.compile("(<.*?(?<!!)>)")

test_str = removeDoubleNeg.sub('', test_str)
test_str = removeTrash.sub('', test_str)

print('Start ' + test_str + '\n')
print('\n' + str(score_groups(test_str)))
