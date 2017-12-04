def part_1():
    #digits = '1234'

    i = open("inputs/day1.txt", "r")
    digits = i.readline().strip()
    i.close()

    digLen = len(digits)
    captchaSum = 0
    for i in range(0,digLen):
        if digits[i] == digits[(i+1) % digLen]:
            captchaSum += int(digits[i])
    print(captchaSum)
part_1()

def part_2():
    #digits = '12131415'

    i = open("inputs/day1.txt", "r")
    digits = i.readline().strip()
    i.close()

    digLen = len(digits)
    captchaSum = 0
    for i in range(0,digLen):
        if digits[i] == digits[(i+digLen//2) % digLen]:
            captchaSum += int(digits[i])
    print(captchaSum)
part_2()
