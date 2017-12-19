def p(i, s):
    pos = 0
    max1 = 0
    for v in range(1,i+1):
        pos = (pos+s)%v+1
        if pos == 1: max1 = v
    print(max1)
    return pos

steps = 329
cb = [0]
curPos = 0
for val in range(1,2018):
    pos = (curPos+steps)%val+1
    cb.insert(pos, val)
    curPos = pos
i = cb.index(2017)
print(cb[i+1])

p(50000000, steps)
